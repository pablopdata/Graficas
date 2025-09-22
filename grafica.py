from flask import Flask, Response
import matplotlib
matplotlib.use('Agg')  # Importante para servidores sin entorno gráfico
import matplotlib.pyplot as plt
import seaborn as sns
import io

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Gráfico simple con Flask y Seaborn</h1>
        <imgt.png
    '''

@app.route('/plot.png')
def plot_png():
    # Usamos seaborn para un gráfico bonito
    sns.set(style="darkgrid")
    plt.figure(figsize=(4,3))
    datos_x = [1, 2, 3, 4]
    datos_y = [1, 4, 9, 16]
    sns.lineplot(x=datos_x, y=datos_y, marker='o')
    plt.title('Ejemplo de gráfico con Seaborn')
    plt.xlabel('X')
    plt.ylabel('Y')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return Response(buf.getvalue(), mimetype='image/png')

if __name__ == '__main__':
    app.run()
