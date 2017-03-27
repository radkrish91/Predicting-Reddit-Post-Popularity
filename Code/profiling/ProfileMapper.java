import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class ProfileMapper extends Mapper<LongWritable, Text, Text, Text>{

        private static final String columnHeader[] = new String[] {"id", "title", "url", "num_points", "num_comments", "author", "created_at"};

    @Override
    public void map(LongWritable key, Text value, Context context) throws IOException, InterruptedException {
        String line = value.toString();
        String []elements = line.split(",");
        context.write(new Text(columnHeader[0]), new Text("Type~BigInt~Value~" + String.valueOf(elements[0])));
        context.write(new Text(columnHeader[1]), new Text("Type~String~Length~" + String.valueOf(elements[1]).length()));
        context.write(new Text(columnHeader[2]), new Text("Type~String~Length~" + String.valueOf(elements[2]).length()));
        context.write(new Text(columnHeader[3]), new Text("Type~BigInt~Value~" + String.valueOf(elements[3])));
        context.write(new Text(columnHeader[4]), new Text("Type~BigInt~Value~" + String.valueOf(elements[4])));
        context.write(new Text(columnHeader[5]), new Text("Type~String~Length~" + String.valueOf(elements[5]).length()));
        context.write(new Text(columnHeader[6]), new Text("Type~String~Value~" + String.valueOf(elements[6])));
    }
}
