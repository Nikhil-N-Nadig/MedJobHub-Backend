from medjobhub import app,db
from medjobhub.models import User
if __name__ == '__main__':
    with app.app_context():
        # db.drop_all()
        db.create_all()
        
        users = User.query.all()
        for user in users:
            user.is_verified = False
        db.session.commit()

    app.run(debug=True, port=5001)
