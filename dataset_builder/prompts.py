_output_guidelines = """
## Output guidelines
- Use tailwindcss for styling
- Generated section should include a title, a description, call to action button, placeholder image, and a navbar.
- Only generate the section, starting with the <section> tag. Do not generate the entire HTML document.
- The output should be only an HTML, in plain text. Do not wrap the output in JSON formatting or triple backticks.
"""

amateur_designer = f"""Imagine you are an amateur website designer. Your task is to generate a poorly designed website that follows the provided guidelines.

## CSS design guidelines
- Use poor inconsistent spacing decisions
- Use low contrast or very sharp jarring colours
- Use an imbalanced typescale

{_output_guidelines}
"""

pro_designer = """Imagine you are an professional website designer. Your task is to generate a well designed website that follows the provided guidelines.

## CSS design guidelines
- Use consistent spacing decisions
- Use a harmonious colour palette
- Use a balanced typescale

{_output_guidelines}
"""

