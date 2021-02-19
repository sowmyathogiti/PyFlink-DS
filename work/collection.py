from pyflink.common.serialization import SimpleStringEncoder
from pyflink.common.typeinfo import Types
from pyflink.datastream.connectors import StreamingFileSink
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment, DataTypes
from pyflink.table.descriptors import Schema, OldCsv, FileSystem
from pyflink.table.udf import udf
def collectionsOfNumbers():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_python_requirements("./input","./output")
    ds = env.from_collection(
        collection=[[1], [2]],
        type_info=Types.ROW([Types.INT()]))
    ds.map((lambda x : x[0]*10))
    ds.add_sink(StreamingFileSink
                .for_row_format('./', SimpleStringEncoder())
                .build())
    env.execute("tutorial_job")

if __name__ == '__main__':
    collectionsOfNumbers()
