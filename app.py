from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
# Route for the "use now" page where users can input a topic
@app.route('/use_now', methods=['GET', 'POST'])
def use_now():
    if request.method == 'POST':
        # Retrieve user input from the form
        topic = request.form['topic']
        grade = request.form['grade']
        board = request.form['board']

        # Create the prompt for the AI model
        prompt_message = (
            f"Tell me more about {topic} and explain it to me as if I am in {grade} grade, studying in {board} board. "
            "Give me a simple explanation of the topic, a cross-question for better understanding, "
            "an example related to the topic, and tips to understand it better."
        )

        def generate_response():
            response_text = ""
            try:
                # Use ollama API to get the streaming response from the AI model
                stream = ollama.chat(
                    model="llama3.1",
                    messages=[
                        {"role": "user", "content": prompt_message}
                    ],
                    stream=True  # Enable streaming
                )

                # Collect each chunk of the response
                for chunk in stream:
                    response_text += chunk['message']['content']
            except ollama.ResponseError as e:
                response_text = f"Error: {str(e)}"
            return response_text

        # Get AI response
        response_text = generate_response()
        return jsonify({'response': response_text, 'topic': topic})

    return render_template('use_now.html')

if __name__ == '__main__':
    app.run(debug=True)
