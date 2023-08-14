from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return "Welcome to PG-Ditiss"
    
@app.route("/modules", methods=["GET"])
def sh_modules():
    return "1.FCN, 2.Security Concepts, 3.COSA, 4.NDC, 5.PKI 6,ITIL & Devops, 7.Compliance Audit"
    
@app.route("/institute", methods=["GET"])
def sh_details():
    return "Name: Sunbeam Institute Of Information Technology, Address: Hinjewadi,pune "
    
app.run(host="0.0.0.0", port=4000, debug=True)
