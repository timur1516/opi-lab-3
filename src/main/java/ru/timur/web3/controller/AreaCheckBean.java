package ru.timur.web3.controller;

import jakarta.enterprise.context.SessionScoped;
import ru.timur.web3.entity.PointEntity;
import ru.timur.web3.view.InputBean;

import java.io.Serializable;
import java.util.Date;

/**
 * Компонент с сессионной областью видимости для обработки пользовательского
 * ввода и проверки попадания точки в заданную область.
 * Реализует логику обработки координат и радиуса, а также проверяет, попадает
 * ли точка в заданную геометрическую область.
 */
@SessionScoped
public class AreaCheckBean implements Serializable {

    /**
     * Обрабатывает пользовательский ввод, создает сущность точки и определяет,
     * попадает ли она в заданную область.
     *
     * @param input объект {@link InputBean}, содержащий входные данные (координаты
     *              x, y и радиус r)
     * @return объект {@link PointEntity}, содержащий координаты, радиус, время
     *         выполнения, результат проверки попадания и время вычисления
     */
    public PointEntity processInput(InputBean input) {
        PointEntity pointEntity = new PointEntity();
        pointEntity.setTime(new Date());
        pointEntity.setX(input.getX());
        pointEntity.setY(input.getY());
        pointEntity.setR(input.getR());

        long startTime = System.nanoTime() / 1000;
        pointEntity.setHit(isHit(pointEntity.getX(), pointEntity.getY(), pointEntity.getR()));
        long endTime = System.nanoTime() / 1000;
        pointEntity.setCalculationTime(endTime - startTime);
        return pointEntity;
    }

    /**
     * Проверяет, попадает ли точка с координатами (x, y) в заданную область,
     * определенную радиусом r.
     * Область включает:
     * - Четверть круга в первом квадранте (x ≥ 0, y ≥ 0, x² + y² ≤ r²).
     * - Треугольник во втором квадранте (x ≤ 0, y ≥ 0, y ≤ 2x + r).
     * - Прямоугольник в четвертом квадранте (x ∈ [-r, 0], y ∈ [-r/2, 0]).
     *
     * @param x координата x точки
     * @param y координата y точки
     * @param r радиус, определяющий размеры области
     * @return {@code true}, если точка попадает в область, {@code false} — в
     *         противном случае
     */
    public boolean isHit(double x, double y, double r) {
        return x * x + y * y <= r * r && y >= 0 && x >= 0 ||
                y <= 2 * x + r && y >= 0 && x <= 0 ||
                -r <= x && x <= 0 && -r / 2 <= y && y <= 0;
    }
}