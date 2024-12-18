# %%
import my_sql_module as msm

PGHOST = '...'
PGDATABASE = '...'
PGUSER = '...'
PGPASSWORD = '..'

# %%
# Una conexión para todo el programa
conn = msm.create_server_connection(PGHOST, PGDATABASE, PGUSER, PGPASSWORD)

# %%
def total_de_pedidos_unicos():

    cur = None

    data = None

    SQL = 'SELECT COUNT(DiSTINCT checkNumber) FROM payments'
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
        if conn: conn.rollback()
    finally:
        if cur:
            cur.close()

    return data[0][0]


resultado = total_de_pedidos_unicos()

print(resultado)

# %%
def obtener_items_x_venta_ddbb():
    cur = None
    data = None

    SQL = 'SELECT  DISTINCT orderNumber, orderlinenumber, quantityOrdered  FROM sales GROUP BY orderNumber,orderlinenumber ORDER BY orderNumber'
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()

    return data


def cantidad_media_de_items():
    data = obtener_items_x_venta_ddbb()

    curr_order = None
    qitems_x_venta = {}
    suma_items_pedidos = 0

    for (ordn, lordn, q) in data:
        if ordn != curr_order:
            curr_order = ordn
            qitems_x_venta[ordn] = 0

        qitems_x_venta[ordn] += q
        suma_items_pedidos += q

    media = round(suma_items_pedidos/len(qitems_x_venta), 2)

    return media, qitems_x_venta


media, iventas = cantidad_media_de_items()
print('media:',media)
print('ventas:', iventas)

# %%
import statistics as st

def clientes_credito_mayor_a(valor, esMayor):
    cur = None
    data = None

    simbolo = '>'
    if not esMayor: simbolo = '<='

    SQL = 'SELECT  c.* from customers c WHERE c.creditlimit {0} {1}'.format(
        simbolo, valor)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()

    return data


def getClientesMediaVarianza(valor, esMayor=True):
    clientes = clientes_credito_mayor_a(valor, esMayor)

    lcredits = list(map(lambda aRow: float(aRow[-1]), clientes))

    return clientes, st.mean(lcredits), st.variance(lcredits)


clientes, media, varianza = getClientesMediaVarianza(1000)
print('clientes:', clientes)
print('media:', media)
print('varianza:', varianza)

# %%
clientes, media, varianza = getClientesMediaVarianza(1000, esMayor=False)
print('clientes:', clientes)
print('media:', media)
print('varianza:', varianza)

# %%
# Cerramos conexión global
if conn: conn.close()


