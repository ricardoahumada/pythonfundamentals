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
def pagos_mayores_a(valor):

    cur = None

    data = None

    SQL = 'SELECT * FROM payments WHERE amount > ' + str(valor)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()

    return data


resultado = pagos_mayores_a(100)
print(resultado)

# %%
def pagos_mayores_y_cliente(valor, customer):

    cur = None

    data = None

    SQL = 'SELECT * FROM payments WHERE amount > ' + str(valor) + ' AND customerNumber = '+ str(customer)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()

    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()

    return data


resultado = pagos_mayores_y_cliente(100, 103)
print(resultado)

# %%
def clientes_nombre_comiencen_o_terminen(texto):

    cur = None

    data = None

    SQL = "SELECT * FROM customers WHERE LOWER(customerName) LIKE '{0}%' OR LOWER(customerName) LIKE '%{0}'".format(texto)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()

    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()
        

    return data


resultado = clientes_nombre_comiencen_o_terminen('a')
print(resultado)

# %%
def actualiza_codigo_postal_para_ciudad(new_cp, city):

    cur = None

    isOK = False

    SQL = "UPDATE customers SET postalcode = {0} WHERE LOWER(city) LIKE '%{1}%'".format(
        new_cp, city)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        conn.commit()
        isOK = True
    except Exception as err:
        print(f"Error: '{err}'")
        if conn:
            conn.rollback()
    finally:
        if cur:
            cur.close()

    return isOK


resultado = actualiza_codigo_postal_para_ciudad(10005, 'las')
print(resultado)

# %%
def show_data_for_fields(campos, valor):

    cur = None

    data = None

    SQL = "SELECT {0} FROM sales WHERE sales_amount>={1} ORDER BY sales_amount ASC".format(','.join(campos), valor)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()
        

    return data


lcampos = ('orderNumber', 'status', 'sales_amount')
resultado = show_data_for_fields(lcampos, 100)
print(resultado)

# %%
def pagos_agrupados_por_cliente_con_compra():

    cur = None

    data = None

    SQL = """SELECT DISTINCT p.customerNumber, p.checkNumber, p.paymentDate, p.amount FROM payments p 
LEFT JOIN sales s ON s.customerNumber=p.customerNumber WHERE s.customerNumber IS NOT NULL ORDER BY p.customerNumber"""
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()
        

    return data


resultado = pagos_agrupados_por_cliente_con_compra()
print(resultado)

# %%
def ventas_productos_x_texto_cp(texto, cp):

    cur = None

    data = None

    SQL = """SELECT s.*, p.productName, c.postalCode FROM sales s 
LEFT JOIN products p ON (s.productCode = p.productCode) 
LEFT JOIN customers c ON s.customerNumber=c.customerNumber 
WHERE p.productName LIKE '%{0}%' AND c.postalCode = '{1}'""".format(texto, cp)
    print('SQL:', SQL)

    try:
        cur = conn.cursor()
        cur.execute(SQL)
        data = cur.fetchall()
    except Exception as err:
        print(f"Error: '{err}'")
    finally:
        if cur:
            cur.close()
        

    return data


resultado = ventas_productos_x_texto_cp('ar', 60528)
print(resultado)

# %%
# Cerramos conexión global
if conn: conn.close()


