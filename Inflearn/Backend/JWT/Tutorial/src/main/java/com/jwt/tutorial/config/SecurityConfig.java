package com.jwt.tutorial.config;

import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;

@EnableWebSecurity // 기본적인 Web 보안을 활성화 하겠다.
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    @Override
    public void configure(WebSecurity web) throws Exception {
        web
                .ignoring()
                .antMatchers(
                        "/h2-console/**",           // h2 console 하위 모든 요청은 spring security 로직을 수행하지 않는다.
                        "/favicon.ico",                        // favicon 관련도 로직을 구행하지 않는다.
                        "/error"
                );
    }

    @Override
    protected void configure(HttpSecurity http) throws Exception {
        http
                .authorizeHttpRequests()                          // HttpServletRequest를 사용하는 요청들에 대한 접근제한을 설정한다.
                .antMatchers("/api/hello").permitAll() // antMatchers(path).permitAll() > path에 대한 내용은 인증없이 접근을 허용한다.
                .anyRequest().authenticated();                    // 그외 모든 요청은 모두 인증이 필요하다.
    }
}
