from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

board = dict(size=3)

@app.route("/", methods=["GET", "POST"])
def students_page():
    # if request.method == "POST":
        # new_student = Student(name=new_student_name, lastname=new_student_lastname)
        # students.append(new_student)
        # return redirect(url_for("students_page"))

    return render_template("index.html", board=board)


if __name__ == "__main__":
    app.run(debug=True)
