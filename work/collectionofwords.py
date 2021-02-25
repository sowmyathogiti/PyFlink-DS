from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream.connectors import StreamingFileSink
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
from pyflink.table.udf import udf
def collectionOfWords():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)
    t_env = StreamTableEnvironment.create(env)

    add = udf(lambda i: "text : "+ i + " | len : " +str(len(i)), [ DataTypes.STRING()], DataTypes.STRING())

    t_env.register_function("add", add)

    t_env.connect(FileSystem().path('./input.txt')) \
        .with_format(OldCsv() \
                     .field('i', DataTypes.STRING())) \
        .with_schema(Schema() \
                     .field('i', DataTypes.STRING())) \
        .create_temporary_table('mySource')

    t_env.connect(FileSystem().path('./output.txt')) \
        .with_format(OldCsv()
                     .field('rsl', DataTypes.STRING())) \
        .with_schema(Schema()
                     .field('rsl', DataTypes.STRING())) \
        .create_temporary_table('mySink')

    t_env.from_path('mySource') \
        .select("add(i)") \
        .insert_into('mySink')

    t_env.execute("tutorial_job")

if __name__ == '__main__':
    collectionOfWords()