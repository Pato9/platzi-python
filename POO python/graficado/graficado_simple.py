

from bokeh.plotting import figure, output_file,show



if __name__ == '__main__':
    output_file('graficado_simple.html')

    x_vals = ["uno","dos","tres","cuatro"]
    y_vals = []

    fig = figure(x_range=x_vals,plot_height=250,title="Venta meses",toolbar_location=None)

    for x in x_vals:
        val = int(input(f'Ingrese el valor para :  {x}'))
        y_vals.append(val)
    print(y_vals)

    fig.vbar(x=x_vals,top=y_vals,width=0.9)

    show(fig)


