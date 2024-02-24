# java_selenium_functions.py

import os


def create_java_selenium_project(project_directory):
    # check environment
    os.system(
        f"mvn archetype:generate -DgroupId=com.example -DartifactId=selenium-test -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false"
    )

    with open(f"{project_directory}/pom.xml", "a") as pom_file:
        pom_file.write(
            """
<dependencies>
    <dependency>
        <groupId>org.seleniumhq.selenium</groupId>
        <artifactId>selenium-java</artifactId>
        <version>3.141.59</version>
    </dependency>
    <dependency>
        <groupId>junit</groupId>
        <artifactId>junit</artifactId>
        <version>4.12</version>
    </dependency>
</dependencies>
"""
        )

    os.makedirs(f"{project_directory}/src/test/java", exist_ok=True)

    with open(f"{project_directory}/src/test/java/SeleniumTest.java", "w") as test_file:
        test_file.write(
            """
import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class SeleniumTest {

    @Test
    public void testExample() {
        WebDriver driver = new ChromeDriver();
        driver.get("https://example.com");
        assert driver.getTitle().equals("Example Domain");
        driver.quit();
    }
}
"""
        )
