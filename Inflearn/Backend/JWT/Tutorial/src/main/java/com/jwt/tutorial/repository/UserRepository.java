package com.jwt.tutorial.repository;

import com.jwt.tutorial.entity.User;
import org.springframework.data.jpa.repository.EntityGraph;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    // JpaRepository를 extends 함으로서 findAll, save 등의 methods를 활용할 수 있게 됨.

    /**
     * annotation : Lazy가 아닌 Eager 조회로 authorities 를 함께 가져옴.
     * methoed naem : username을 기분으로 User 정보를 가져오는데 authorities 정보도 함꼐 가져오라는 의미
     * */
    @EntityGraph(attributePaths = "authorities")
    Optional<User> findOneWithAuthoritiesByUsername(String username);

}
