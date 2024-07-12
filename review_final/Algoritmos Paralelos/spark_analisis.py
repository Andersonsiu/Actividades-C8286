from pyspark.sql import SparkSession

def main():
    spark = SparkSession.builder.appName("Big Data Analysis").getOrCreate()

    # Leer el conjunto de datos grande
    data = spark.read.csv("large_dataset.csv", header=True, inferSchema=True)

    # Realizar transformaciones y acciones
    filtered_data = data.filter(data['column'] > 0)
    result = filtered_data.groupBy('column').count()

    # Mostrar los resultados
    result.show()

    spark.stop()

if __name__ == "__main__":
    main()
