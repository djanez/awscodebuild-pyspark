Cuando trabajas con Apache Spark, necesitas una SparkSession para crear DataFrames.
En vez de crearla en cada test (malo, lento, repetitivo), la defines una sola vez en conftest.py.

Scope:
Significa: Se crea una sola vez para toda la ejecución. No se levanta Spark en cada test. Mucho más rápido.

Otros scopes:

"function" → uno por test
"module" → uno por archivo
"session" → uno global
Para Spark → normalmente "session".
