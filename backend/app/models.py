from app import app


class Food(app.db.Model):
    __abstract__ = True

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


class Cereals(Food):
    __tablename__ = 'cereais_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Vegetables(Food):
    __tablename__ = 'verduras_hortalicas_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Fruits(Food):
    __tablename__ = 'frutas_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Fats(Food):
    __tablename__ = 'gorduras_e_oleos'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Seafood(Food):
    __tablename__ = 'pescados_e_frutos_do_mar'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Meet(Food):
    __tablename__ = 'carnes_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Dairy(Food):
    __tablename__ = 'leite_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Drinks(Food):
    __tablename__ = 'bebidas'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Eggs(Food):
    __tablename__ = 'ovos_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Sugar(Food):
    __tablename__ = 'produtos_acucarados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Miscellaneous(Food):
    __tablename__ = 'miscelaneas'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Industrialized(Food):
    __tablename__ = 'outros_alimentos_industrializados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Prepared(Food):
    __tablename__ = 'alimentos_preparados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class Legumes(Food):
    __tablename__ = 'leguminosas_e_derivados'
    id = app.db.Column('index', app.db.Integer, primary_key=True)


class NutsAndSeeds(Food):
    __tablename__ = 'nozes_e_sementes'
    id = app.db.Column('index', app.db.Integer, primary_key=True)
