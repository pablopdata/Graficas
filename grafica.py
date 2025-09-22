from flask import Flask, Response
import matplotlib.pyplot as plt
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Gráfico simple con Flask y Matplotlib</h1>
        /plot.png
    '''

@app.route('/plot.png')
def plot_png():
    # Crear un gráfico simple
    plt.figure(figsize=(4,3))
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], marker='o')
    plt.title('Ejemplo de gráfico')
    plt.xlabel('X')
    plt.ylabel('Y')

    # Guardar el gráfico en un buffer de memoria
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()

