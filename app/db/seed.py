from app.db.database import SessionLocal
from app.db.models.producer import Producer
from app.db.models.property import Property
from app.db.models.harvest import Harvest
from app.db.models.crop import Crop


def seed_data():
    db = SessionLocal()

    try:
        # PRODUTOR 1
        joao = Producer(name="João da Silva", cpf_cnpj="588.466.280-71")
        db.add(joao)
        db.flush()

        propriedade_joao = Property(
            name="Fazenda do João",
            city="Ribeirão Preto",
            state="SP",
            total_area=100.0,
            agricultural_area=60.0,
            vegetation_area=30.0,
            producer_id=joao.id,
        )
        db.add(propriedade_joao)
        db.flush()

        for i in range(1, 4):
            safra = Harvest(name=f"Safra {i} João", property_id=propriedade_joao.id)
            db.add(safra)
            db.flush()

            for j in range(1, 4):
                cultura = Crop(
                    culture_name=f"Cultura {j} João Safra {i}", harvest_id=safra.id
                )
                db.add(cultura)

        # PRODUTOR 2
        maria = Producer(name="Maria Oliveira", cpf_cnpj="008.163.290-87")
        db.add(maria)
        db.flush()

        for p in range(1, 3):  # duas propriedades
            propriedade_maria = Property(
                name=f"Sítio da Maria {p}",
                city="Uberlândia",
                state="MG",
                total_area=80.0 + p * 10,
                agricultural_area=50.0 + p * 5,
                vegetation_area=20.0,
                producer_id=maria.id,
            )
            db.add(propriedade_maria)
            db.flush()

            for i in range(1, 4):  # três safras
                safra = Harvest(
                    name=f"Safra {i} Maria Prop {p}", property_id=propriedade_maria.id
                )
                db.add(safra)
                db.flush()

                for j in range(1, 4):  # três colheitas
                    cultura = Crop(
                        culture_name=f"Cultura {j} Maria P{p} S{i}",
                        harvest_id=safra.id,
                    )
                    db.add(cultura)

        db.commit()
        print("✅ Seed de dados executado com sucesso!")
    except Exception as e:
        db.rollback()
        print("❌ Erro ao aplicar seed:", e)
    finally:
        db.close()


if __name__ == "__main__":
    seed_data()
