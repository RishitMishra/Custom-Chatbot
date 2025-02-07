from flask import Flask, request, jsonify
from flask_cors import CORS
from vectorstore_handler import create_vectorstore
from data_processing import extract_course_names

app = Flask(__name__)
CORS(app)



with app.app_context():
    try:
        url = "https://brainlox.com/courses/category/technical" 
        css_selector = "div.courses-content > h3 > a"
        course_names = extract_course_names(url, css_selector) 
        vector_store = create_vectorstore(course_names)
        
    except Exception as e:
        print(f"Error loading vectorstore: {e}")

@app.route('/chat', methods=['POST'])
def chat():
    
    try:
        
        user_input = request.json.get('query')
        
        if not user_input:
            return jsonify({"error": "Missing query in request body"}), 400

        similar_courses_search = vector_store.similarity_search(query=user_input, k=5)
        similar_courses = []
        for i in similar_courses_search:
            i = i.page_content.split(" URL:")
            similar_courses.append(i)
        return jsonify({"similar_courses": similar_courses})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')