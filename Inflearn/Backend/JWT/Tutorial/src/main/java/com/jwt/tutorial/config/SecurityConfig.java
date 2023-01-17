package com.jwt.tutorial.config;

import com.jwt.tutorial.jwt.*;
import org.springframework.context.annotation.Bean;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.builders.WebSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityConfigurerAdapter;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

@EnableWebSecurity // 기본적인 Web 보안을 활성화 하겠다.
@EnableMethodSecurity(prePostEnabled = true) // @PreAuthorize annotation을 메소드단위로 추가하기 위해 적용
public class SecurityConfig extends WebSecurityConfigurerAdapter {

    // JWT Token과 관련된 내용을 주입
    private final TokenProvider tokenProvider;
    private final JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint;
    private final JwtAccessDeniedHandler jwtAccessDeniedHandler;

    public SecurityConfig(
            TokenProvider tokenProvider,
            JwtAuthenticationEntryPoint jwtAuthenticationEntryPoint,
            JwtAccessDeniedHandler jwtAccessDeniedHandler
    ) {
        this.tokenProvider = tokenProvider;
        this.jwtAuthenticationEntryPoint = jwtAuthenticationEntryPoint;
        this.jwtAccessDeniedHandler = jwtAccessDeniedHandler;
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        // password encoder 설정
        return new BCryptPasswordEncoder();
    }

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
                .csrf().disable()                       // jwt token 방식을 위해 csrf를 diable 함.

                .exceptionHandling()                                    // Exception Handler를 추가 설정함.
                .authenticationEntryPoint(jwtAuthenticationEntryPoint)  // 401 에러
                .accessDeniedHandler(jwtAccessDeniedHandler)            // 403 에러

                // h2-console을 위한 설정을 추가함.
                .and()
                .headers()
                .frameOptions()
                .sameOrigin()

                // session 설정을 추가함. (현재는 사용하지 않기에 Stateless 상태)
                .and()
                .sessionManagement()
                .sessionCreationPolicy(SessionCreationPolicy.STATELESS)

                .and()
                .authorizeHttpRequests()                          // HttpServletRequest를 사용하는 요청들에 대한 접근제한을 설정한다.
                .antMatchers("/api/hello").permitAll() // antMatchers(path).permitAll() > path에 대한 내용은 인증없이 접근을 허용한다.
                .antMatchers("/api/authenticate").permitAll()
                .antMatchers("/api/signup").permitAll()// 상동.
                .anyRequest().authenticated()                     // 그외 모든 요청은 모두 인증이 필요하다.

                .and()
                .apply(new JwtSecurityConfig(tokenProvider));     // JWT Security Config 설정 추가
    }
}
