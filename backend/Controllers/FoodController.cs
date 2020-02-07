using System.Collections.Generic;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using LimosAPI.Model;
using System.Linq;
using System;
using Microsoft.EntityFrameworkCore.Metadata;
using System.Reflection;
using Microsoft.AspNetCore.Cors;

namespace LimosAPI.Controllers
{
    [ApiController]
    [EnableCors("AllowOrigin")]
    [Route("api/[controller]")]
    public class FoodController : ControllerBase
    {
        private readonly dataContext _context;

        public FoodController(dataContext context) => _context = context;

        [HttpGet]
        public ActionResult<IEnumerable<Food>> GetFood()
        {
            string search = Request.Query["search"];

            if (search == null)
            {
                var response = new Dictionary<string, string>
                {
                    { "log", "Missing param `search`" }
                };

                return BadRequest(response);
            }

            var query = _context.Food.Where(
                c => c.Description.ToLower().Contains(search.ToLower()));

            if (query.Count() == 0)
            {
                var response = new Dictionary<string, string>
                {
                    { "log", string.Format("Could not find any items with substring `{0}`", search) }
                };

                return NoContent();
            }

            var arrayFood = new Dictionary<string, long?>() {};

            foreach (var item in query)
            {
                arrayFood.Add(item.Description, item.Id);
            }

            return Ok(arrayFood);
        }

        [HttpGet("{id}")]
        public ActionResult<Food> GetFoodItem(int id)
        {
            var foodItem = _context.Food.Where(c => c.Id == id);

            if (foodItem.Count() == 0)
            {
                var response = new Dictionary<string, string>
                {
                    { "log", string.Format("Could not find any item with id `{0}`", id) }
                };

                return NotFound(response);
            }

            return Ok(foodItem);
        }

        [HttpGet("options")]
        public ActionResult<Food> GetOptions()
        {
            var result = _context.Model.FindEntityType(typeof(Food))
                .GetProperties()
                .Select(property => property.GetColumnName())
                .ToList();

            return Ok(result);
        }
    }
}
