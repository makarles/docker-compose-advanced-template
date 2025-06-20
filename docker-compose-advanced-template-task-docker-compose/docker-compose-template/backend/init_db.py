from base import Base, engine, SessionLocal, User

Base.metadata.create_all(bind=engine)

def seed():
    session = SessionLocal()
    if session.query(User).count() == 0:
        users = [
            User(login='pavel', email='a@gmail.com', hashed_password='pavel_hash'),
            User(login='yura', email='b@gmail.com', hashed_password='yura_hash')
        ]
        session.add_all(users)
        session.commit()
    session.close()

if __name__ == "__main__":
    seed()
