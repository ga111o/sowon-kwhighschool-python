from flask import Flask, render_template_string

app = Flask(__name__)


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.readlines()


@app.route('/')
def index():
    house_lines = read_file('house_prices.txt')
    income_lines = read_file('median_income.txt')

    total_lines = min(len(house_lines), len(income_lines), 5)

    content = []

    for i in range(total_lines):
        content.append(
            f'<p>{i} - House Price: {house_lines[i].strip()} 억 원</p>')
        content.append(
            f'<p>{i} - Income: {income_lines[i].strip()} 천만 원</p>')
        content.append('<hr/>')

    final_content = ''.join(content)

    return render_template_string('''
        <style>
            body {
                -webkit-user-select: none; /* Chrome/Safari */
                -moz-user-select: none; /* Firefox */
                -ms-user-select: none; /* IE/Edge */
                user-select: none; /* Non-prefixed version, currently
                supported by Chrome, Opera, and Edge */
            }
        </style>
        <script>
            document.addEventListener('contextmenu', function(e) {
                e.preventDefault(); // 오른쪽 클릭 메뉴 비활성화
            });
            document.addEventListener('selectstart', function(e) {
                e.preventDefault(); // 텍스트 선택 비활성화
            });
            document.addEventListener('copy', function(e) {
                e.preventDefault(); // 복사 비활성화
            });
        </script>
        <h1>House Prices and Median Income</h1>
        <p># The California housing dataset is a well-known dataset provided by the California Department of <br/>
            # Housing and Community Development (HCD). It is commonly used for regression tasks in machine <br/>
            # learning and can be found in the scikit-learn library.
        </p>
        {{ content|safe }}
    ''', content=final_content)


@app.route('/n/<int:num>')
def show_data(num):
    house_lines = read_file('house_prices.txt')
    income_lines = read_file('median_income.txt')

    total_lines = min(len(house_lines), len(income_lines))

    if num > total_lines:
        num = total_lines

    content = []
    content.append(f'<h2>{num} data</h2>')

    for i in range(num):
        content.append(f'<p>{i} - House Price: {house_lines[i].strip()}</p>')
        content.append(
            f'<p>{i} - Income: {income_lines[i].strip()}</p>')
        content.append('<hr/>')
        if (i + 1) % 10 == 0:
            content.append('<p>!광고 글!</p>')
            content.append('<p>!광고 글!</p>')
            content.append('<p>!광고 글!</p>')
            content.append('<p>!광고 글!</p>')
            content.append('<p>!광고 글!</p>')

    final_content = ''.join(content)

    return render_template_string('''
        <style>
            body {
                -webkit-user-select: none; /* Chrome/Safari */
                -moz-user-select: none; /* Firefox */
                -ms-user-select: none; /* IE/Edge */
                user-select: none; /* Non-prefixed version, currently
                supported by Chrome, Opera, and Edge */
            }
        </style>
        <script>
            document.addEventListener('contextmenu', function(e) {
                e.preventDefault(); // 오른쪽 클릭 메뉴 비활성화
            });
            document.addEventListener('selectstart', function(e) {
                e.preventDefault(); // 텍스트 선택 비활성화
            });
            document.addEventListener('copy', function(e) {
                e.preventDefault(); // 복사 비활성화
            });
        </script>
        <h1>House Prices and Median Income</h1>
        {{ content|safe }}
    ''', content=final_content)


if __name__ == '__main__':
    app.run(debug=True)
