"""
AI Module Summarization Backend Server
Flask API for generating module summaries from curriculum JSON
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend integration

# Map subjects to curriculum files
CURRICULUM_FILES = {
    'mathematics': 'mathematics_curriculum.json',
    'aiml': 'aiml_curriculum.json',
    'programming_c': 'programming_c_curriculum.json'
}

CURRICULUM_CACHE = {}

def load_curriculum(subject='mathematics'):
    """Load curriculum for specified subject"""
    if subject in CURRICULUM_CACHE:
        return CURRICULUM_CACHE[subject]
    
    if subject not in CURRICULUM_FILES:
        return None
    
    curriculum_path = os.path.join(os.path.dirname(__file__), '..', CURRICULUM_FILES[subject])
    try:
        with open(curriculum_path, 'r', encoding='utf-8') as f:
            curriculum = json.load(f)
            CURRICULUM_CACHE[subject] = curriculum
            return curriculum
    except FileNotFoundError:
        print(f"Error: Curriculum file not found: {curriculum_path}")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON in curriculum file: {curriculum_path}")
        return None

def format_summary(module_data):
    """
    Format module content according to AI chatbot summarization template
    
    Args:
        module_data: Dictionary containing module information
        
    Returns:
        Dictionary with formatted summary sections
    """
    core = module_data.get('core_content', {})
    exam = module_data.get('exam_orientation', {})
    
    summary = {
        'module_name': module_data.get('module_name', 'Unknown Module'),
        'level': module_data.get('level', 'Unknown'),
        'module_summary': extract_module_summary(core.get('theory', '')),
        'key_concepts': extract_key_concepts(core.get('theory', '')),
        'intuition': core.get('intuition', 'Understanding gained through practice and application.'),
        'worked_examples': core.get('worked_examples', []),
        'common_mistakes': core.get('common_mistakes', []),
        'exam_takeaways': exam.get('tips', []),
        'real_world_applications': core.get('real_world_applications', [])
    }
    
    return summary

def extract_module_summary(theory_text):
    """Extract 2-3 sentence summary from theory text"""
    if not theory_text:
        return "No summary available."
    
    # Take first 200-300 characters as summary
    sentences = theory_text.split('. ')
    summary_sentences = []
    char_count = 0
    
    for sentence in sentences[:3]:
        if char_count + len(sentence) < 300:
            summary_sentences.append(sentence)
            char_count += len(sentence)
        else:
            break
    
    return '. '.join(summary_sentences) + '.' if summary_sentences else theory_text[:300] + '...'

def extract_key_concepts(theory_text):
    """Extract key concepts from theory text"""
    # Simple extraction - look for definitions and key statements
    concepts = []
    
    if 'is a' in theory_text or 'are' in theory_text:
        sentences = theory_text.split('. ')
        for sentence in sentences[:10]:  # First 10 sentences likely contain key concepts
            if any(keyword in sentence.lower() for keyword in ['is a', 'is an', 'are', 'means', 'represents']):
                if len(sentence) < 200:  # Keep it concise
                    concepts.append(sentence.strip())
            if len(concepts) >= 6:  # Limit to 6 key concepts
                break
    
    # Fallback: generic concepts
    if not concepts:
        concepts = [
            "Core concepts covered in this module",
            "Fundamental principles and definitions",
            "Key techniques and methods",
            "Important formulas and relationships"
        ]
    
    return concepts

@app.route('/api/summarize', methods=['POST'])
def summarize_module():
    """
    API endpoint to generate module summary
    
    Request JSON format:
    {
        "subject": "mathematics",  # or "aiml" or "programming_c"
        "module_id": "linear_equations",
        "level": "beginner"
    }
    
    Response JSON format:
    {
        "success": true,
        "summary": { ... formatted summary ... }
    }
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({
                'success': False,
                'error': 'No data provided'
            }), 400
        
        subject = data.get('subject', 'mathematics')  # Default to mathematics
        module_id = data.get('module_id')
        level = data.get('level')
        
        if not module_id or not level:
            return jsonify({
                'success': False,
                'error': 'module_id and level are required'
            }), 400
        
        # Load curriculum for subject
        curriculum = load_curriculum(subject)
        if not curriculum:
            return jsonify({
                'success': False,
                'error': f'Failed to load curriculum for subject: {subject}'
            }), 500
        
        # Find the requested module
        modules = curriculum.get('levels', {}).get(level, {}).get('modules', [])
        module = None
        
        for m in modules:
            if m.get('module_id') == module_id:
                module = m
                break
        
        if not module:
            return jsonify({
                'success': False,
                'error': f'Module {module_id} not found at {level} level in {subject}'
            }), 404
        
        # Generate summary
        summary = format_summary(module)
        
        return jsonify({
            'success': True,
            'summary': summary
        })
    
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({
            'success': False,
            'error': 'Internal server error'
        }), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'module-summarization-api'
    })

@app.route('/api/subjects', methods=['GET'])
def list_subjects():
    """List all available subjects"""
    subjects = [
        {'id': 'mathematics', 'name': 'Mathematics'},
        {'id': 'aiml', 'name': 'AI & Machine Learning'},
        {'id': 'programming_c', 'name': 'Programming in C'}
    ]
    return jsonify({
        'success': True,
        'subjects': subjects
    })

@app.route('/api/modules', methods=['GET'])
def list_modules():
    """List all available modules for a subject"""
    subject = request.args.get('subject', 'mathematics')
    
    try:
        curriculum = load_curriculum(subject)
        if not curriculum:
            return jsonify({
                'success': False,
                'error': f'Failed to load curriculum for subject: {subject}'
            }), 500
        
        modules_list = []
        for level_name, level_data in curriculum.get('levels', {}).items():
            for module in level_data.get('modules', []):
                modules_list.append({
                    'module_id': module.get('module_id'),
                    'module_name': module.get('module_name'),
                    'level': level_name,
                    'subject': subject
                })
        
        return jsonify({
            'success': True,
            'subject': subject,
            'modules': modules_list,
            'total': len(modules_list)
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    print("=" * 60)
    print("Module Summarization API Starting...")
    print("=" * 60)
    
    # Verify curriculum files exist
    base_path = os.path.dirname(__file__)
    for subject, filename in CURRICULUM_FILES.items():
        filepath = os.path.join(base_path, '..', filename)
        if os.path.exists(filepath):
            print(f"✓ {subject.upper()} curriculum found")
        else:
            print(f"✗ WARNING: {subject.upper()} curriculum not found at {filepath}")
    
    print("\nAPI Endpoints:")
    print("  POST /api/summarize  - Generate module summary")
    print("  GET  /api/modules    - List all modules")
    print("  GET  /api/health     - Health check")
    print("\nStarting server on http://localhost:5000")
    print("=" * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
