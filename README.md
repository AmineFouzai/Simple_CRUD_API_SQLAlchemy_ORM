# Simple_CRUD_API_SQLAlchemy_ORM
<p>Simple CRUD API  Build With  <a href="https://www.tornadoweb.org/en/stable/">Tornado</a>  Framework And SQLAlchemy_ORM  For mapping any SQL Database</p>

------------------------------------

# setup: 
<table>
<tr>
<td> 1)  git clone https://github.com/MedAmineFouzai/Simple_CRUD_API_SQLAlchemy_ORM </td>
</tr>
<tr>
<td> 2) cd Simple_CRUD_API_SQLAlchemy_ORM</td>
</tr>
<tr>
<td> 3) pip install pipenv</td>
</tr>
</tr>
<td> 4) pipenv --python 3.6</td>
</tr>
<tr>
<td> 5) pipenv install - r requirements.txt</td>
</tr>
<tr>
  <td>
    6) run project with <a href="https://pypi.org/project/torn/">torn cli</a> : <b>#command: [ torn run ] </b>  </td>
 </tr>
</table>

-----------------------------------

<img src="https://github.com/MedAmineFouzai/Simple_CRUD_API_SQLAlchemy_ORM/blob/master/Captures/sqla_logo.png">

[SQLAlchemy](https://pypi.org/project/SQLAlchemy/) is an open-source SQL toolkit and object-relational mapper for the Python programming language

-----------------------------------

# Connecting To A Database:
change uri to the suited database (postgresql,oracl,mysql,...) in
[models/post.py](https://github.com/MedAmineFouzai/Simple_CRUD_API_SQLAlchemy_ORM/blob/master/models/post.py)

    ex:[mysql+pymysql://root:@localhost/dbname]


```python
DB_NAME="MyDatabaseName"
engine=create_engine('mysql+pymysql://root:@localhost/{}'.format(DB_NAME),echo=False)
Base=declarative_base()
session=Session(bind=engine)

```
----------------------------------------------

# Defining Object Data:

change the Columns and there data types based on your object fields

## ex:

 ```python
 class post(Base):
 
    __tablename__='posts'
    id=Column(Integer,primary_key=True)
    title=Column(String(50))
    body=Column(String(50))
    
    def __repr__(self):
        return "<Post(id={},title={},body={}>".format(self.id,self.title,self.body)
 ```
  
