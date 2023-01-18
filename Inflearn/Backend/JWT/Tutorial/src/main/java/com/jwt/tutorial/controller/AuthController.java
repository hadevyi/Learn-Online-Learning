package com.jwt.tutorial.controller;

import com.jwt.tutorial.dto.*;
import com.jwt.tutorial.jwt.JwtFilter;
import com.jwt.tutorial.jwt.TokenProvider;
import org.springframework.http.*;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.config.annotation.authentication.builders.AuthenticationManagerBuilder;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;

@RestController
@RequestMapping("/api")
public class AuthController {
    private final TokenProvider tokenProvider;
    private final AuthenticationManagerBuilder authenticationManagerBuilder;

    public AuthController(TokenProvider tokenProvider, AuthenticationManagerBuilder authenticationManagerBuilder) {
        this.tokenProvider = tokenProvider;
        this.authenticationManagerBuilder = authenticationManagerBuilder;
    }

    @PostMapping("/authenticate")
    public ResponseEntity<TokenDto> authorize(@Valid @RequestBody LoginDto loginDto) {
        // 사용자가 입력한 username과 password를 활용해 authentication token을 만든다.
        UsernamePasswordAuthenticationToken authenticationToken =
                new UsernamePasswordAuthenticationToken(loginDto.getUsername(), loginDto.getPassword());

        // 해당 내용을 통해 CustomUserDetailsService을 지나서 (정상적이라면,) authentication 정보를 가져와서,
        Authentication authentication = authenticationManagerBuilder.getObject().authenticate(authenticationToken);
        // security context에 저장을 한다.
        SecurityContextHolder.getContext().setAuthentication(authentication);

        // 이 작업들을 통해 가져온 내용을 provider를 활용해 실제 token으로 만들어주고,
        String jwt = tokenProvider.createToken(authentication);

        // response header에도 넣어주며,
        HttpHeaders httpHeaders = new HttpHeaders();
        httpHeaders.add(JwtFilter.AUTHORIZATION_HEADER, "Bearer " + jwt);

        // return하게 된다.
        return new ResponseEntity<>(new TokenDto(jwt), httpHeaders, HttpStatus.OK);
    }
}
