package ru.timur.web3.entity;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.io.Serializable;
import java.util.Date;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor

@Entity
@Table(name = "ARCHIVE")
public class PointEntity implements Serializable, Comparable<PointEntity> {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "ID")
    private long id;

    @Column(name = "X", nullable = false)
    private double x;

    @Column(name = "Y", nullable = false)
    private double y;

    @Column(name = "R", nullable = false)
    private double r;

    @Column(name = "HIT", nullable = false)
    private boolean hit;

    @Column(name = "TIME", nullable = false)
    private Date time;

    @Column(name = "CALC_TIME", nullable = false)
    private long calculationTime;

    @Column(name = "SESSION_ID", nullable = false)
    private String sessionId;

    @Override
    public int compareTo(PointEntity o) {
        if (this.id == o.id)
            return 0;
        return this.id < o.id ? -1 : 1;
    }
}
