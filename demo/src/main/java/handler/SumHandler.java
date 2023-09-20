package handler;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;
import domain.User;

import java.io.File;
import java.io.IOException;
import java.io.OutputStream;
public class SumHandler implements HttpHandler {

    @Override
    public void handle(HttpExchange e) throws IOException {
        String filePath = "/Users/kms/Desktop/cote/demo/data/user.json";

        ObjectMapper objectMapper = new ObjectMapper();
        User[] users = objectMapper.readValue(new File(filePath), User[].class);

        int sum = 0;
        for (User user : users) {
            sum += user.getPost_count();
        }

        String jsonResponse = "{\"sum\":\"" + sum +"\"}";

        e.getResponseHeaders().add("Content-Type", "application/json");
        e.sendResponseHeaders(200, jsonResponse.length());

        System.out.println("Sum 값 전송");

        try(OutputStream os = e.getResponseBody()) {
            os.write(jsonResponse.getBytes());
        }

    }
}
