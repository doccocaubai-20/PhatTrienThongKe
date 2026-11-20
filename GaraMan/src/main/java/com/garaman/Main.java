package com.garaman;

import java.io.File;
import org.apache.catalina.WebResourceRoot;
import org.apache.catalina.core.StandardContext;
import org.apache.catalina.startup.Tomcat;
import org.apache.catalina.webresources.DirResourceSet;
import org.apache.catalina.webresources.StandardRoot;

public class Main {
    public static void main(String[] args) throws Exception {
        int port = 8080;
        Tomcat tomcat = new Tomcat();
        tomcat.setPort(port);
        tomcat.setBaseDir("temp");
        tomcat.getConnector();

        File docBase = new File("WebContent");
        if (!docBase.exists()) {
            docBase = new File("C:/Users/admin/Documents/GaraMan/WebContent");
        }

        StandardContext ctx = (StandardContext) tomcat.addWebapp("", docBase.getAbsolutePath());
        ctx.setParentClassLoader(Main.class.getClassLoader());

        File additionWebInfClasses = new File("target/classes");
        if (!additionWebInfClasses.exists()) {
            additionWebInfClasses = new File("C:/Users/admin/Documents/GaraMan/target/classes");
        }

        if (additionWebInfClasses.exists()) {
            WebResourceRoot resources = new StandardRoot(ctx);
            resources.addPreResources(new DirResourceSet(resources, "/WEB-INF/classes",
                    additionWebInfClasses.getAbsolutePath(), "/"));
            ctx.setResources(resources);
        }

        System.out.println("Live server at: localhost:" + port);

        tomcat.start();
        tomcat.getServer().await();
    }
}
