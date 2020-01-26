from app import app


class Food(app.db.Model):
    __tablename__ = 'food'

    id = app.db.Column('index', app.db.Integer, primary_key=True)
    description = app.db.Column('Descrição', app.db.String)
    humidity = app.db.Column('Umidade (%)', app.db.Float)
    energy_kcal = app.db.Column('Energia (kcal)', app.db.Integer)
    energy_kj = app.db.Column('Energia (kJ)', app.db.Integer)
    protein = app.db.Column('Proteína (g)', app.db.Float)
    fat = app.db.Column('Lipídeos (g)', app.db.Float)
    cholesterol = app.db.Column('Colesterol (mg)', app.db.Float)
    carbs = app.db.Column('Carboidrato (g)', app.db.Float)
    fiber = app.db.Column('Fibra Alimentar (g)', app.db.Float)
    calcium = app.db.Column('Cálcio (mg)', app.db.Float)
    magnesium = app.db.Column('Magnésio (mg)', app.db.Float)
    manganese = app.db.Column('Manganés (mg)', app.db.Float)
    phosphorus = app.db.Column('Fósforo (mg)', app.db.Float)
    iron = app.db.Column('Ferro (mg)', app.db.Float)
    sodium = app.db.Column('Sódio (mg)', app.db.Float)
    potassium = app.db.Column('Potássio (mg)', app.db.Float)
    copper = app.db.Column('Cobre (mg)', app.db.Float)
    zinc = app.db.Column('Zinco (mg)', app.db.Float)
    retinol = app.db.Column('Retinol (mcg)', app.db.Float)
    thiamine = app.db.Column('Tiamina (mg)', app.db.Float)
    riboflavin = app.db.Column('Riboflavina (mg)', app.db.Float)
    pyridoxine = app.db.Column('Piridoxina (mg)', app.db.Float)
    niacin = app.db.Column('Niacina (mg)', app.db.Float)
    vitamin_c = app.db.Column('Vitamina C (mg)', app.db.Float)
    category = app.db.Column('Categoria', app.db.String)


class FoodSchema(app.ma.ModelSchema):
    class Meta: model = Food
