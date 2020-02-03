using System;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata;

namespace LimosAPI.Model
{
    public partial class dataContext : DbContext
    {
        public dataContext()
        {
        }

        public dataContext(DbContextOptions<dataContext> options)
            : base(options)
        {
        }

        public virtual DbSet<Food> Food { get; set; }

        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlite("Data Source=Data/data.db");
            }
        }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            modelBuilder.Entity<Food>(entity =>
            {
                entity.HasNoKey();

                entity.ToTable("food");

                entity.HasIndex(e => e.Id)
                    .HasName("ix_food_index");
                
                entity.Property(e => e.Id)
                    .HasColumnName("index")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Description)
                    .HasColumnName("Descrição")
                    .HasColumnType("STRING");

                entity.Property(e => e.Carbs)
                    .HasColumnName("Carboidrato (g)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Copper)
                    .HasColumnName("Cobre (mg)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Cholesterol)
                    .HasColumnName("Colesterol (mg)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Calcium)
                    .HasColumnName("Cálcio (mg)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.EnergyKJ)
                    .HasColumnName("Energia (kJ)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.EnergyKcal)
                    .HasColumnName("Energia (kcal)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Iron)
                    .HasColumnName("Ferro (mg)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Fiber)
                    .HasColumnName("Fibra Alimentar (g)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Phosphorus)
                    .HasColumnName("Fósforo (mg)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Fat)
                    .HasColumnName("Lipídeos (g)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Magnesium)
                    .HasColumnName("Magnésio (mg)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Manganese)
                    .HasColumnName("Manganés (mg)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Niacin).HasColumnName("Niacina (mg)");

                entity.Property(e => e.Pyridoxine).HasColumnName("Piridoxina (mg)");

                entity.Property(e => e.Potassium)
                    .HasColumnName("Potássio (mg)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Protein)
                    .HasColumnName("Proteína (g)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.Retinol).HasColumnName("Retinol (mcg)");

                entity.Property(e => e.Riboflavin).HasColumnName("Riboflavina (mg)");

                entity.Property(e => e.Sodium)
                    .HasColumnName("Sódio (mg)")
                    .HasColumnType("BIGINT");

                entity.Property(e => e.Thiamine).HasColumnName("Tiamina (mg)");

                entity.Property(e => e.Humidity)
                    .HasColumnName("Umidade (%)")
                    .HasColumnType("FLOAT");

                entity.Property(e => e.VitaminC).HasColumnName("Vitamina C (mg)");

                entity.Property(e => e.Zinc)
                    .HasColumnName("Zinco (mg)")
                    .HasColumnType("FLOAT");
                
                entity.Property(e => e.Category)
                    .HasColumnName("Categoria")
                    .HasColumnType("STRING");
            });

            OnModelCreatingPartial(modelBuilder);
        }

        partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
    }
}
