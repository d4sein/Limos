using System;
using System.Collections.Generic;

namespace LimosAPI.Model
{
    public partial class Food
    {
        public long? Id { get; set; }
        public string Description { get; set; }
        public double? Humidity { get; set; }
        public long? EnergyKcal { get; set; }
        public long? EnergyKJ { get; set; }
        public double? Protein { get; set; }
        public double? Fat { get; set; }
        public double? Cholesterol { get; set; }
        public double? Carbs { get; set; }
        public string Fiber { get; set; }
        public long? Calcium { get; set; }
        public long? Magnesium { get; set; }
        public double? Manganese { get; set; }
        public long? Phosphorus { get; set; }
        public double? Iron { get; set; }
        public long? Sodium { get; set; }
        public long? Potassium { get; set; }
        public string Copper { get; set; }
        public double? Zinc { get; set; }
        public string Retinol { get; set; }
        public string Thiamine { get; set; }
        public string Riboflavin { get; set; }
        public string Pyridoxine { get; set; }
        public string Niacin { get; set; }
        public string VitaminC { get; set; }
        public string Category { get; set; }
    }
}
