package com.example.demo;

import com.sun.net.httpserver.HttpServer;
import handler.CheckHandler;
import handler.SumHandler;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.io.IOException;
import java.net.InetSocketAddress;

@SpringBootApplication
public class DemoApplication {

	public static void main(String[] args) throws IOException {
		String hostname = "0.0.0.0";
		int port = 5678;

		HttpServer server = HttpServer.create(new InetSocketAddress(hostname, port), 0);

		server.createContext("/", new CheckHandler());
		server.createContext("/sum", new SumHandler());

		server.setExecutor(null);
		server.start();

		System.out.println("HTTP 서버가 " + hostname + ":" + port + " 에서 실행되었습니다.");
	}
}
