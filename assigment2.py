from flask import Flask
app = Flask (__name__)

Filey = open(file=r"C:\Users\moren\OneDrive\Desktop\Resume\DMorenoResume.html", mode='r')
webString = Filey.read()

@app.route('/')
def hello_world():
    return webString

if __name__ == '__main__':
    app.run()   


