# Automated Certificate Generator

This Program was built inorder to automate the sports day certificate generator process for my college.
If you are planning to use it go through README file and mdoify code.

## Features
- Generates certificates automatically from a template.
- Substitutes values for Name, Class, Semester, and Event from a CSV file.
- Converts the generated Word documents to PDF format.

## Requirements

- Python 3.x
- Required Python libraries: `os`, `csv`, `docx`, `docx2pdf`

## Usage

1. Clone the repository:

```
gh repo clone xreedev/Automated-Certificate-Generator
```

2. Place your certificate template as `template.docx` in the project directory with NAME ,CLASS and EVENT to be substituted.

3. Place your CSV file with the data (containing columns Name, Class, Semester, Event) in the directory `student_data`.

4. Install requirements.txt and run the program:

```
pip install -r requirements.txt
```

5. Find your generated certificates in the `Final_Certificates` directory.

## Modification

If you need to modify the certificate template, make sure to leave the placeholders `NAME`, `CLASS`, `SEM`, and `EVENT` where the values need to be substituted. With minimal experience, you can modify the code to suit your use case.
<br>This is the template.

![template](template.png "Certificate Template")<br>
This is the final result.

![Certificate](final.png "Certificate ")

## Note

This program was created to automate the certificate designing process for my college. No coding experience is needed to use this program, just basic understanding.I just built to automate design which was supposed to be done by me manually.
Any contributions are welcome.

## Support

For any issues or queries, feel free to contact Sreedev TS at [xreedev@gmail.com](mailto:xreedev@gmail.com).

Enjoy automating your certificate generation process!
