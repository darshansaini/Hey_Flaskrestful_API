from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")

def Home():
    return "<h3> Flask API for :</h3>" \
           "<p>1.prime numbers within given range(type /prime/your number in address bar)</p>"\
           "<p>1.Prime factors of given number(type /primefactor/your number in address bar)</p>"



@app.route("/prime/<int:a>")
def prime(a):
    lis = []
    for i in range(2, a + 1):
        flag = 0
        for j in range(2, i // 2):
            if i % j == 0:
                flag = 1
                break
        if flag == 0:
            lis.append(i)

    result = {
        "prime numbers within the range" : lis

    }
    return  jsonify(result)

@app.route("/primefactor/<int:a>")
def primefactor(a):
    print("the prime of", a, "are", end=' ')
    b = []
    d = 2
    while a > 1:
        while a % d == 0:
            b.append(d)
            a = a // d
        d += 1

    return {
        "prime factors of the number " : b
    }

if __name__ == '__main__':
    
    app.run(debug=True)