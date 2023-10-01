from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('ex.html')

@app.route('/process_data', methods=['POST','GET'])
def process_data():
    my_value = request.form['my_value']
   

    return "Value received: " + my_value

if __name__ == '__main__':
    app.run()


<script>
  function saveOption() {
    var selectElement = document.getElementById("options");
    var selectedValue = selectElement.value;
    // Perform further actions with the selected value
    console.log(selectedValue);
    // Save the value to local storage or a cookie if needed
  }
</script>