from flask import Blueprint, render_template, jsonify, current_app
import stripe

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return "API Stripe com Flask"

@main.route("/pagamento")
def pagamento():
    return render_template("pagamento.html", public_key=current_app.config['STRIPE_PUBLIC_KEY'])

@main.route("/criar-sessao", methods=["POST"])
def criar_sessao():
    # Agora dentro do contexto da aplicação
    stripe.api_key = current_app.config.get("STRIPE_SECRET_KEY")
    
    try:
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "brl",
                    "unit_amount": 5000,
                    "product_data": {"name": "Curso de Programação"},
                },
                "quantity": 1,
            }],
            mode="payment",
            success_url="http://localhost:5000/sucesso",
            cancel_url="http://localhost:5000/cancelado",
        )
        return jsonify({"sessionId": session.id})
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@main.route("/sucesso")
def sucesso():
    return "✅ Pagamento realizado com sucesso!"

@main.route("/cancelado")
def cancelado():
    return "⚠️ Pagamento cancelado."

