from flask import Flask,render_template
FAI=Flask(__name__)

@FAI.route('/firsthtml')

def firsthtml():
    return render_template('first.html')
@FAI.route('/secondhtml')
def secondhtml():
    return render_template('data_render.html',name='Advaith',age=2,Location='Bangalore')

FAI.run(debug=True)      