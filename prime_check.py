# Program to check if a number is prime or not
from flask import Flask, request, render_template_string, session
app = Flask(__name__)
num = 29

# To take input from the user
#num = int(input("Enter a number: "))

# define a flag variable

@app.route('/', methods=['GET', 'POST'])
def prime_value():
    flag = False

    if num == 1:
        print(num, "is not a prime number")
    elif num > 1:
        # check for factors
        for i in range(2, num):
            if (num % i) == 0:
                # if factor is found, set flag to True
                flag = True
                # break out of loop
                break

        # check if flag is True
        if flag:
            print(num, "is not a prime number")
        else:
            print(num, "is a prime number")
    return render_template_string('''
        <html>
            <body>
                <p>Guess a number between 1 and 100:</p>
                <form method="post">
                    <input type="text" name="guess"/>
                    <input type="submit" value="Guess"/>
                </form>
                <p>{{ message }}</p>
            </body>
        </html>
    ''', message=message)
if __name__ == '__main__':
    app.run(debug=True)
