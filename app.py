
from flask import Flask, render_template, request, redirect, url_for, flash

from flask_mysqldb import MySQL


# conexion MySQL
app=Flask(__name__, template_folder='templates')
app.config['MYSQL_HOST']='sql10.freemysqlhosting.net'
app.config['MYSQL_USER']='sql10500057'
app.config['MYSQL_PASSWORD']='Yq963gTDhQ'
app.config['MYSQL_DB']='sql10500057'
mysql=MySQL(app)

#configurar sesion 
app.secret_key='mysecretkey'


@app.route('/')
def Index():
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data=cur.fetchall()
    return render_template("Index.html", contacts=data)

@app.route('/add_contact', methods=['POST'])
def Add_contact():
    if request.method=='POST':
        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES(%s,%s,%s)', (fullname, phone,email))
        mysql.connection.commit()
        flash('Contacto agregado satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/edit/<id>')
def get_contact(id):
   # print(id)
    cur=mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id={0}' .format(id))
    data=cur.fetchall()
    return render_template('edit_contact.html', contact=data[0])
    
    
@app.route('/delete/<string:id>')
def Delete_contact(id):
    cur=mysql.connection.cursor()
    cur.execute('DELETE FROM contacts WHERE id={0}'.format(id))
    mysql.connection.commit()
    flash('Contacto Eliminado Satisfactoriamente')
    return redirect(url_for('Index'))


@app.route ('/update/<id>', methods=['POST']) #@app.route('/add_contact', methods=['POST'])
def update_contact(id):
    if request.method=='POST':
        fullname=request.form['fullname']
        phone=request.form['phone']
        email=request.form['email']
        print( fullname,phone,email,id)
        cur=mysql.connection.cursor()
        cur.execute('UPDATE contacts SET fullname=%s, phone=%s, email=%s WHERE id=%s', (fullname, phone, email,id))
        mysql.connection.commit()
        flash('Contacto actualizado satisfactoriamente')
        return redirect(url_for('Index'))

@app.route('/planes')
def planes():
    datos=[]
    with open('p10k12w01.txt') as fname:
        lineas=fname.readlines()
        for linea in lineas:
            datos.append(linea.strip('\n'))
            #datos=datos+linea
     
    return render_template('/planes.html', value=datos)



if __name__=='__main__':
    
    app.run(host='0.0.0.0')
