import json
import os

def load_blueprint(file_path):
    with open(file_path) as f:
        return json.load(f)

def generate_pipeline(blueprint):
    lang = blueprint["language"]
    ci_file = ".github/workflows/ci.yml"
    template_parts = []

    template_parts.append("templates/common/lint.yml")
    template_parts.append("templates/common/test.yml")
    template_parts.append("templates/common/deploy.yml")

    lang_template = f"templates/{lang}.yml"
    if os.path.exists(lang_template):
        template_parts.insert(1, lang_template)

    with open(ci_file, "w") as target:
        target.write("name: CI Pipeline\non:\n  push:\n    branches: [main, dev]\n  pull_request:\n\njobs:\n")
        for file in template_parts:
            with open(file) as f:
                target.write(f.read())
                target.write("\n")

    print(f"✅ Generated {ci_file} for {blueprint['project_name']}")

if __name__ == "__main__":
    blueprint = load_blueprint("blueprints/sample-project.json")
    generate_pipeline(blueprint)
    #test completed
