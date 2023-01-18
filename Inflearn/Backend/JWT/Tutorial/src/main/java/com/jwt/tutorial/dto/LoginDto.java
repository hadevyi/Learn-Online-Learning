package com.jwt.tutorial.dto;

import lombok.*;
import javax.validation.constraints.*;

@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor  // lombok 관련 annotation
public class LoginDto {

    @NotNull
    @Size(min = 3, max = 50) // valid 관련 annotation
    private String username;

    @NotNull
    @Size(min = 3, max = 100)
    private String password;
}
