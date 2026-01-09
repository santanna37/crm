from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey, Table, DateTime
from src.infra.db.settings.base import Base
from sqlalchemy.orm import relationship
from datetime import datetime



class PersonEntity(Base):
    __tablename__ = "person"

    id = Column(Integer, primary_key= True, autoincrement= True)
    full_name = Column(String(100))
    email = Column(String(100))
    birth_date = Column(Date)
    phone = Column(String(50))
    consent = Column(Boolean, default= False)
    created_at = Column(DateTime, default= datetime.utcnow, nullable= False)
    activate = Column(Boolean, default= True)

    address = relationship("AddressEntity", back_populates = 'person', uselist= False)

    themes = relationship('Themes', secondary = "themes_person", back_populates = "person")


    def __repr__(self):
        return f"Person [id= {self.id}, name= {self.full_name}]"



class AddressEntity(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key= True, autoincrement= True)
    cep = Column(String(10))
    street = Column(String(100)) # rua 
    number = Column(String(10)) # numero
    complement = Column(String(10)) # complemento
    burgh = Column(String(50)) # bairro 
    city = Column(String(50)) # municipio
    state_uf = Column(String(2)) # UF
    state_name = Column(String(50)) # estado nome
    id_person = Column(Integer, ForeignKey('person.id')) 

    person = relationship('PersonEntity', back_populates = 'address')

    def __repr__(self):
        return f"Address: {self.street} , {self.number}"


themes_person = Table(
    'themes_person',
    Base.metadata,
    Column('id', Integer, primary_key = True, autoincrement = True),
    Column('id_person', Integer, ForeignKey('person.id')),
    Column('id_themes', Integer, ForeignKey('themes.id'))
)


class Themes(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key = True, autoincrement = True)
    code = Column(String(50), unique= True, nullable = False)
    description = Column(String(50))

    person = relationship("PersonEntity", secondary = "themes_person", back_populates = 'themes')

