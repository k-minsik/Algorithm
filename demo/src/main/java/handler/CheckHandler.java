package handler;

import com.sun.net.httpserver.HttpExchange;
import com.sun.net.httpserver.HttpHandler;

import java.io.IOException;
import java.io.OutputStream;

public class CheckHandler implements HttpHandler {

    @Override
    public void handle(HttpExchange e) throws IOException {
        String jsonResponse = "{\"message\":\"server check\"}";

        e.getResponseHeaders().add("Content-Type", "application/json");
        e.sendResponseHeaders(200, jsonResponse.length());

        System.out.println("Check 메세지 전송");

        try(OutputStream os = e.getResponseBody()) {
            os.write(jsonResponse.getBytes());
        }
    }
}
