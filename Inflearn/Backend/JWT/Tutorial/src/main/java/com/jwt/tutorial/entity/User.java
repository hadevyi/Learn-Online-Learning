package com.jwt.tutorial.entity;

import com.fasterxml.jackson.annotation.JsonIgnore;
import lombok.*;
import javax.persistence.*;
import java.util.*;

@Entity                     // Databse의 Table과 1:1 Mapping되는 Object
@Table(name = "`user`")     // Table 이름을 지정하기 위함
@Getter
@Setter
@Builder
@AllArgsConstructor
@NoArgsConstructor           // 상단은 Lombok Annotation으로 활용됨 (실무에서는 더 상세히 확인)
public class User {

    @JsonIgnore
    @Id                                                 // PK 설정
    @Column(name = "user_id")                           // 현재 사용하는 변수명과 별개의 Table Column Name
    @GeneratedValue(strategy = GenerationType.IDENTITY) // AutoIncrement
    private Long userId;

    @Column(name = "username", length = 50, unique = true)
    private String username;

    @Column(name = "password", length = 100)
    private String password;

    @Column(name = "nickname", length = 50)
    private String nickname;

    @Column(name = "activated")
    private boolean activated;

    @ManyToMany     // User - User_authority - authority 의 다대다 관계를 각각 일대다/다대일의 조인 테이블로 정의함
    @JoinTable(
            name = "user_authority",
            joinColumns = {@JoinColumn(name = "user_id", referencedColumnName = "user_id")},
            inverseJoinColumns = {@JoinColumn(name = "authority_name", referencedColumnName = "authority_name")})
    private Set<Authority> authorities;
}