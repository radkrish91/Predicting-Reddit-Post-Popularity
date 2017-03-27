import java.io.IOException;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;

import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class ProfileReducer extends Reducer<Text, Text, Text, Text>{

        public static String findRange(Iterable<Text> values) {
                int max = Integer.MIN_VALUE;
                int min = Integer.MAX_VALUE;
                for (Text value : values) {
                String stringValue = value.toString();
                String []elements = stringValue.split("~");
                int val = Integer.parseInt(elements[3].trim());
                if(val < min) {
                        min = val;
                }

                if(val > max) {
                        max = val;
                }
        }
                return "Type:BigInt, Minimum: " + String.valueOf(min) + ", Maximum: " + String.valueOf(max);
        }

        public static String findMax(Iterable<Text> values) {
                int maxValue = Integer.MIN_VALUE;
                for (Text value : values) {
                        String stringValue = value.toString();
                String []elements = stringValue.split("~");
                        int val = Integer.parseInt(elements[3].trim());
                        maxValue = Math.max(maxValue, val);
                }
                return "Type:String, MaxLength: " + String.valueOf(maxValue);
        }

        public static String findMinMaxDate(Iterable<Text> values) {
                SimpleDateFormat f = new SimpleDateFormat("mm/dd/yy hh:mm");
                long min = Long.MAX_VALUE;
                long max = Long.MIN_VALUE;
                for(Text value : values) {
                        String stringValue = value.toString();
                        String []elements = stringValue.split("~");
                        String date = elements[3].trim();
                        Date d;
                        try {
                                d = f.parse(date);
                                long milliseconds = d.getTime();
                                if(milliseconds < min) {
                                        min = milliseconds;
                                }
                                if(milliseconds > max) {
                                        max = milliseconds;
                                }
                        } catch (ParseException e) {
                                e.printStackTrace();
                        }
                }
                Date d2 = new Date(min);
                Date d3 = new Date(max);
                return "Type:Date, MinDate: " + String.valueOf(d2) + ", MaxDate: " + String.valueOf(d3);
        }

        @Override
    public void reduce(Text key, Iterable<Text> values, Context context) throws IOException, InterruptedException {
                String columnHeader = key.toString();
                switch(columnHeader) {
                        case "id":
                                String idFormatter = findRange(values);
                                context.write(key, new Text(idFormatter));
                                break;
                        case "title":
                                String titleFormatter = findMax(values);
                                context.write(key, new Text(titleFormatter));
                                break;
                        case "url":
                                String urlFormatter = findMax(values);
                                context.write(key, new Text(urlFormatter));
                                break;
                        case "num_points":
                                String pointsFormatter = findRange(values);
                                context.write(key, new Text(pointsFormatter));
                                break;
                        case "num_comments":
                                String commentsFormatter = findRange(values);
                                context.write(key, new Text(commentsFormatter));
                                break;
                        case "author":
                                String authorFormatter = findMax(values);
                                context.write(key, new Text(authorFormatter));
                                break;
                        case "created_at":
                                String createdFormatter = findMinMaxDate(values);
                                context.write(key, new Text(createdFormatter));
                                break;
                        default:
                            break;
            }
        }
}

