import csv
import argparse
from datetime import datetime

def procesar_csv(archivo_csv, archivo_salida):
    with open(archivo_csv, newline='', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file)
        cabecera = next(csv_reader)

        # Verificar si la cabecera tiene la estructura esperada
        if cabecera != ["Booking date", "Value date", "Transactions Payment details", "Debit", "Credit", "Currency"]:
            print("La cabecera no tiene la estructura esperada.")
            return

        # Inicializar variables para almacenar información
        transacciones = []
        descripcion_actual = None

        for fila in csv_reader:
            if fila and fila[0].strip() and fila[0][0].isdigit():
                # Fila que comienza con una fecha (estructura similar a las filas de datos)
                booking_date, value_date, payment_details, debit, credit, currency = fila

                # Convertir Credit a número flotante
                credit = float(credit.replace(',', '')) if credit else 0.0

                # Modificar la línea de conversión de debit
                if debit:
                    signo_posicion = debit.find('-')
                    if signo_posicion != -1:
                        parte_no_numerica = debit[:signo_posicion].strip()
                        parte_numerica = debit[signo_posicion:].replace(',', '')
                        debit = float(parte_numerica) if parte_numerica else 0.0
                        # Agregar la parte no numérica a payment_details
                        transacciones[-1]["Transaction Payment details"] += " " + parte_no_numerica
                    else:
                        # No hay signo "-", procesar como de costumbre
                        debit = float(debit.replace(',', ''))
                else:
                    debit = 0.0

                descripcion_actual = None  # Reiniciar la descripción

                if payment_details.startswith("Balance of settlement"):
                    transacciones.append({
                        "Booking date": booking_date,
                        "Value date": value_date,
                        "Transaction Payment details": payment_details,
                        "Debit": debit,
                        "Credit": credit,
                        "Currency": currency,
                        "Description": payment_details,
                    })
            else:
                # Fila impar (estructura igual a la fila 3)
                descripcion_actual = fila[0]
                transacciones.append({
                            "Booking date": booking_date,
                            "Value date": value_date,
                            "Transaction Payment details": payment_details,
                            "Debit": debit,
                            "Credit": credit,
                            "Currency": currency,
                            "Description": descripcion_actual  # Asociar la descripción actual
                        })

        # Procesar la información almacenada
        for transaccion in transacciones:
            print("Descripción:", transaccion["Description"])
            print("Booking date:", transaccion["Booking date"])
            print("Value date:", transaccion["Value date"])
            print("Payment details:", transaccion["Transaction Payment details"])
            print("Debit Amount:", transaccion["Debit"])
            print("Credit:", transaccion["Credit"])
            print("Currency:", transaccion["Currency"])
            print("\n")

        # Escribir las transacciones en un nuevo archivo CSV con nombre dinámico
        fecha_hora_actual = datetime.now().strftime("%y%m%d_%H%M%S")
        nombre_archivo_salida = f"{fecha_hora_actual}.csv"

        with open(nombre_archivo_salida, mode='w', newline='', encoding='utf-8') as csv_output:
            csv_writer = csv.writer(csv_output)

            # Escribir la cabecera
            csv_writer.writerow(["Booking date", "Value date", "Transaction Payment details", "Text Debit", "Debit", "Credit", "Currency", "Description"])

            # Escribir cada transacción
            for transaccion in transacciones:
                csv_writer.writerow([
                    transaccion["Booking date"],
                    transaccion["Value date"],
                    transaccion["Transaction Payment details"],
                    transaccion["Debit"],
                    transaccion["Credit"],
                    transaccion["Currency"],
                    transaccion["Description"],
                ])

def main():
    # Configurar el argumento de línea de comandos para el archivo de entrada
    parser = argparse.ArgumentParser(description='Procesar archivo CSV.')
    parser.add_argument('archivo_entrada', help='Nombre del archivo CSV de entrada.')

    # Obtener el nombre del archivo de salida basado en la fecha y hora actuales
    fecha_hora_actual = datetime.now().strftime("%y%m%d_%H%M%S")
    nombre_archivo_salida_predeterminado = f"{fecha_hora_actual}.csv"

    parser.add_argument('--archivo_salida', default=nombre_archivo_salida_predeterminado, help='Nombre del archivo CSV de salida (por defecto se genera automáticamente).')

    # Parsear los argumentos de la línea de comandos
    args = parser.parse_args()

    # Llamar a la función con los argumentos proporcionados
    procesar_csv(args.archivo_entrada, args.archivo_salida)

if __name__ == "__main__":
    main()
