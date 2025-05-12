from flask import Flask, request, jsonify
from models.refeicao import Refeicao
from database import db
from datetime import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "TESTE"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db.init_app(app)


@app.route("/", methods=["GET"])
def refeicao():
    return jsonify({"message": "refeição"})


@app.route("/create", methods=["POST"])
def CreateRefeicao():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    date_time = data.get("date_time")
    within_the_diet = data.get("within_the_diet")

    if name and description and date_time and within_the_diet is not None:
        date_time = datetime.strptime(date_time, "%Y-%m-%dT%H:%M:%S")
        refeicao = Refeicao(
            name=name,
            description=description,
            date_time=date_time,
            within_the_diet=within_the_diet,
        )
        db.session.add(refeicao)
        db.session.commit()
        return jsonify({"message": "Refeição cadastrada com"})


@app.route("/refeicoes", methods=["GET"])
def readRefeicoes():
    refeicoes = Refeicao.query.all()
    refeicoes_json = [
        {
            "id": refeicao.id,
            "name": refeicao.name,
            "description": refeicao.description,
            "date_time": refeicao.date_time.isoformat(),
            "within_the_diet": refeicao.within_the_diet,
        }
        for refeicao in refeicoes
    ]
    return jsonify(refeicoes_json), 200


@app.route("/refeicao/<int:id_refe>", methods=["GET"])
def readRefeicao(id_refe):
    refeicao = Refeicao.query.get(id_refe)
    if refeicao:
        return jsonify(
            {"name": refeicao.name, "descricao": refeicao.description}
        )

    return jsonify({"message": "refeição nao encontrada"})

@app.route("/refeicao/<int:id_refe>", methods=["PUT"])
def putRefeicai(id_refe):
    data = request.json
    refeicao = Refeicao.query.get(id_refe)
    
    if refeicao:
        refeicao.name = data.get("name")
        refeicao.description = data.get("description")
        refeicao.within_the_diet = data.get("within_the_diet")
        db.session.commit()
        
        return jsonify({"message": f"a Refeição {id_refe} atualizado com sucesso"})
    return jsonify({"message": "Refeição nao encontrada não encontrado"}),404


@app.route("/refeicao/<int:id_refe>", methods=["DELETE"])
def deleteRefeicao(id_refe):
    refeicao = Refeicao.query.get(id_refe)
    if refeicao:
        db.session.delete(refeicao)
        db.session.commit()
        return jsonify({"message": f"Refeição {id_refe} deletado com sucesso"})
    return jsonify({"message": "Refeição não encontrado"}), 404
if __name__ == "__main__":
    app.run(debug=True)
