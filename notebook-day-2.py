import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return la, np, plt, sci, scipy


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4], 
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )    
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),                
                )
            )
        ],
        justify="space-around"
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    An equilibrium satisfies :

    \[
    \dot{x}=\dot{y}=\dot{\theta}=0
    \]

    and

    \[
    \ddot{x}=\ddot{y}=\ddot{\theta}=0.
    \]

    Using the system equations tha we found yesterday:

    \[
    \ddot{x}=-f\sin(\theta+\phi)
    \]

    \[
    \ddot{y}=f\cos(\theta+\phi)-g
    \]

    \[
    \ddot{\theta}=-\frac{f}{J}\frac{\ell}{2}\sin(\phi),
    \]

    we first impose

    \[
    \ddot{\theta}=0.
    \]

    Since \(f>0\), we obtain

    \[
    \sin(\phi)=0.
    \]

    Because

    \[
    |\phi|<\frac{\pi}{2},
    \]

    the only possible solution is

    \[
    \phi=0.
    \]

    Then the horizontal equilibrium condition

    \[
    \ddot{x}=0
    \]

    gives

    \[
    \sin(\theta)=0.
    \]

    Since

    \[
    |\theta|<\frac{\pi}{2},
    \]

    the only solution is

    \[
    \theta=0.
    \]

    Finally, the vertical equilibrium condition

    \[
    \ddot{y}=0
    \]

    gives

    \[
    f\cos(0)-g=0.
    \]

    Thus,

    \[
    f=g.
    \]

    Since in our model

    \[
    g=1,
    \]

    we obtain

    \[
    f=1.
    \]

    Therefore, the equilibrium states are

    \[
    (x,0,y,0,0,0),
    \]

    where \(x\) and \(y\) are arbitrary constants, and the corresponding constant inputs are

    \[
    f=1,
    \qquad
    \phi=0.
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We linearize the system around a generic equilibrium

    \[
    s^\star = (x^\star,0,y^\star,0,0,0)
    \]

    with constant equilibrium inputs

    \[
    f^\star = Mg,
    \qquad
    \phi^\star = 0.
    \]

    The nonlinear equations we found are

    \[
    \ddot{x}
    =
    -\frac{f}{M}\sin(\theta+\phi),
    \]

    \[
    \ddot{y}
    =
    \frac{f}{M}\cos(\theta+\phi)-g,
    \]

    \[
    \ddot{\theta}
    =
    -\frac{f\ell}{2J}\sin(\phi).
    \]

    We introduce the error variables

    \[
    \Delta x = x-x^\star,
    \qquad
    \Delta y = y-y^\star,
    \qquad
    \Delta\theta = \theta,
    \]

    and for the inputs

    \[
    \Delta f = f-Mg,
    \qquad
    \Delta\phi = \phi.
    \]

    Equivalently,

    \[
    x = x^\star + \Delta x,
    \qquad
    y = y^\star + \Delta y,
    \qquad
    \theta = \Delta\theta,
    \]

    and

    \[
    f = Mg + \Delta f,
    \qquad
    \phi = \Delta\phi.
    \]


    For small angles, we use the first-order approximations

    \[
    \sin(\Delta\theta+\Delta\phi)
    \approx
    \Delta\theta+\Delta\phi,
    \]

    \[
    \cos(\Delta\theta+\Delta\phi)
    \approx
    1,
    \]

    \[
    \sin(\Delta\phi)
    \approx
    \Delta\phi.
    \]

    We also neglect second-order terms such as

    \[
    \Delta f \,\Delta\theta,
    \qquad
    \Delta f \,\Delta\phi.
    \]

    ---

    Substituting into the horizontal dynamics (found yesterday):

    \[
    \ddot{x}
    =
    -\frac{Mg+\Delta f}{M}
    \sin(\Delta\theta+\Delta\phi),
    \]

    gives

    \[
    \ddot{x}
    \approx
    -\frac{Mg}{M}
    (\Delta\theta+\Delta\phi),
    \]

    thus

    \[
    \Delta\ddot{x}
    =
    -g(\Delta\theta+\Delta\phi).
    \]

    ---

    For the vertical dynamics (found yesterday):

    \[
    \ddot{y}
    =
    \frac{Mg+\Delta f}{M}
    \cos(\Delta\theta+\Delta\phi)-g,
    \]

    and since

    \[
    \cos(\Delta\theta+\Delta\phi)\approx1,
    \]

    we obtain

    \[
    \ddot{y}
    \approx
    \frac{Mg+\Delta f}{M}-g.
    \]

    Because

    \[
    \frac{Mg}{M}=g,
    \]

    the equilibrium terms cancel:

    \[
    \Delta\ddot{y}
    =
    \frac{\Delta f}{M}.
    \]

    ---

    Finally, for the rotational dynamics:

    \[
    \ddot{\theta}
    =
    -\frac{(Mg+\Delta f)\ell}{2J}
    \sin(\Delta\phi),
    \]

    thus

    \[
    \ddot{\theta}
    \approx
    -\frac{Mg\ell}{2J}\Delta\phi,
    \]

    which gives

    \[
    \Delta\ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    ---

    Therefore, the linearized model is

    \[
    \boxed{
    \begin{aligned}
    \Delta\ddot{x} &= -g(\Delta\theta+\Delta\phi),\\
    \Delta\ddot{y} &= \frac{\Delta f}{M},\\
    \Delta\ddot{\theta} &= -\frac{Mg\ell}{2J}\Delta\phi.
    \end{aligned}
    }
    \]
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We use the linear state z,
    and we use error variables because we want to study the behavior of the system near an equilibrium configuration.

    \[
    z =
    \begin{pmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta y \\
    \Delta v_y \\
    \Delta \theta \\
    \Delta \omega
    \end{pmatrix}
    \]

    and the input

    \[
    u =
    \begin{pmatrix}
    \Delta f \\
    \Delta \phi
    \end{pmatrix}.
    \]

    The linearized model is written in standard form as

    \[
    \dot z = Az + Bu.
    \]

    From

    \[
    \Delta\ddot{x} = -g(\Delta\theta+\Delta\phi),
    \]

    \[
    \Delta\ddot{y} = \frac{\Delta f}{M},
    \]

    \[
    \Delta\ddot{\theta} = -\frac{Mg\ell}{2J}\Delta\phi,
    \]

    we get

    \[
    \begin{cases}
    \Delta \dot{x} = \Delta v_x,\\
    \Delta \dot{v}_x = -g\Delta\theta - g\Delta\phi,\\
    \Delta \dot{y} = \Delta v_y,\\
    \Delta \dot{v}_y = \frac{1}{M}\Delta f,\\
    \Delta \dot{\theta} = \Delta \omega,\\
    \Delta \dot{\omega} = -\frac{Mg\ell}{2J}\Delta\phi.
    \end{cases}
    \]

    Therefore,

    \[
    A =
    \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & -g & 0\\
    0 & 0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}
    \]

    and

    \[
    B =
    \begin{pmatrix}
    0 & 0\\
    0 & -g\\
    0 & 0\\
    \frac{1}{M} & 0\\
    0 & 0\\
    0 & -\frac{Mg\ell}{2J}
    \end{pmatrix}.
    \]
    """)
    return


@app.cell
def _(J, M, g, l, np):


    A = np.array([
        [0, 1, 0, 0,  0, 0],
        [0, 0, 0, 0, -g, 0],
        [0, 0, 0, 1,  0, 0],
        [0, 0, 0, 0,  0, 0],
        [0, 0, 0, 0,  0, 1],
        [0, 0, 0, 0,  0, 0],
    ])

    B = np.array([
        [0, 0],
        [0, -g],
        [0, 0],
        [1/M, 0],
        [0, 0],
        [0, -(M*g*l)/(2*J)],
    ])
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The generic equilibrium is not asymptotically stable.
    An equilibrium is asymptotically stable if and only if all eigenvalues of the matrix \(A\)
    have strictly negative real part.

    Here, the matrix \(A\) is

    \[
    A =
    \begin{pmatrix}
    0 & 1 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & -g & 0\\
    0 & 0 & 0 & 1 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 0\\
    0 & 0 & 0 & 0 & 0 & 1\\
    0 & 0 & 0 & 0 & 0 & 0
    \end{pmatrix}.
    \]

    This matrix is nilpotent, so all its eigenvalues are equal to zero:

    \[
    \mathrm{spec}(A)=\{0,0,0,0,0,0\}.
    \]

    Since the eigenvalues do not have strictly negative real parts, the equilibrium is not asymptotically stable.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Yes,The linearized model is controllable, because:

    A linear system $\dot{z} = Az + Bu$ is **controllable** if and only if the
    Kalman controllability matrix:

    $$
    \mathcal{C} = \begin{bmatrix} B & AB & A^2B & A^3B & A^4B & A^5B \end{bmatrix} \in \mathbb{R}^{6 \times 12}
    $$

    has **full row rank** equal to the dimension of the state space., i.e. $\mathrm{rank}(\mathcal{C}) = 6$.
    """)
    return


@app.cell
def _(A, B, np):
    # Build the controllability matrix C = [B, AB, A²B, ..., A⁵B]
    n = A.shape[0]  # state dimension = 6

    C_ctrl = np.hstack([np.linalg.matrix_power(A, k) @ B for k in range(n)])

    rank = np.linalg.matrix_rank(C_ctrl)

    print("Controllability matrix shape:", C_ctrl.shape)
    print(f"Rank of C : {rank}")
    print(f"Required  : {n}")
    print()
    is_controllable = (rank == n)
    print(f"System is controllable: {is_controllable}")
    if is_controllable:
        print()
        print("→ The linearized model is CONTROLLABLE.")
        print("  Any state can be reached from any initial condition.")
        print("  In particular, we can design a stabilizing feedback controller.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    For the reduced lateral system, we keep only

    \[
    z =
    \begin{pmatrix}
    \Delta x \\
    \Delta v_x \\
    \Delta\theta \\
    \Delta\omega
    \end{pmatrix}
    \]

    and we control only with

    \[
    u = \Delta\phi.
    \]

    Since \(f = Mg\), the linearized lateral equations are

    \[
    \Delta\ddot{x}
    =
    -g(\Delta\theta+\Delta\phi),
    \]

    \[
    \Delta\ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    Thus,

    \[
    \begin{cases}
    \Delta\dot{x} = \Delta v_x,\\
    \Delta\dot{v}_x = -g\Delta\theta - g\Delta\phi,\\
    \Delta\dot{\theta} = \Delta\omega,\\
    \Delta\dot{\omega} = -\frac{Mg\ell}{2J}\Delta\phi.
    \end{cases}
    \]

    Therefore,

    \[
    A =
    \begin{pmatrix}
    0 & 1 & 0 & 0\\
    0 & 0 & -g & 0\\
    0 & 0 & 0 & 1\\
    0 & 0 & 0 & 0
    \end{pmatrix},
    \qquad
    B =
    \begin{pmatrix}
    0\\
    -g\\
    0\\
    -\frac{Mg\ell}{2J}
    \end{pmatrix}.
    \]

    To check controllability, we use Kalman's criterion:

    \[
    \mathcal C =
    \begin{pmatrix}
    B & AB & A^2B & A^3B
    \end{pmatrix}.
    \]

    The controllability matrix according to the code below is :
    \[
    \mathcal C =
    \begin{pmatrix}
    0 & -g & 0 & \frac{Mg^2\ell}{2J} \\
    -g & 0 & \frac{Mg^2\ell}{2J} & 0 \\
    0 & -\frac{Mg\ell}{2J} & 0 & 0 \\
    -\frac{Mg\ell}{2J} & 0 & 0 & 0
    \end{pmatrix}.
    \]

    The four columns are linearly independent because none of them can be written as a linear combination of the others.

    Therefore,

    \[
    \operatorname{rank}(\mathcal C)=4=n.
    \]

    Hence, according to Kalman's criterion, the reduced lateral system is controllable.

    ---

    ### Conclusion

    The lateral system is controllable: by acting only on the reactor angle \(\phi\), it is possible to steer the booster from any initial state to any target state.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    # Reduced lateral system: states = [Δx, Δvx, Δθ, Δω], input = [Δφ]
    A_lat = np.array([
        [0,  1,  0,  0],
        [0,  0, -g,  0],
        [0,  0,  0,  1],
        [0,  0,  0,  0],
    ])

    B_lat = np.array([
        [0],
        [-g],
        [0],
        [-(M * g * l) / (2 * J)],
    ])

    # Controllability matrix: [B, AB, A²B, A³B]
    n_lat = A_lat.shape[0]
    C_lat = np.hstack([np.linalg.matrix_power(A_lat, k) @ B_lat for k in range(n_lat)])

    rank_lat = np.linalg.matrix_rank(C_lat)
    print(f"A_lat =\n{A_lat}\n")
    print(f"B_lat =\n{B_lat}\n")
    print(f"Controllability matrix =\n{C_lat}\n")
    print(f"Rank: {rank_lat} / {n_lat}")
    print(f"Lateral system is controllable: {rank_lat == n_lat}")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell
def _(A_lat, np, plt, sci):
    # Conditions initiales : [Δx, Δvx, Δθ, Δω]
    z0 = [0.0, 0.0, np.pi / 4, 0.0]
    t_span = [0.0, 10.0]
    t = np.linspace(t_span[0], t_span[1], 1000)

    # Pas de controle : phi = 0 donc u = 0
    def lateral_free(t, z):
        return A_lat @ z  # B_lat * 0 = 0

    sol = sci.solve_ivp(lateral_free, t_span, z0, dense_output=True)
    z_t = sol.sol(t)

    # Extraction des variables
    delta_x     = z_t[0]
    delta_theta = z_t[2]

    # Graphes
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].plot(t, delta_x, color="steelblue")
    axes[0].set_title(r"Position latérale $\Delta x(t)$")
    axes[0].set_xlabel("temps $t$ (s)")
    axes[0].set_ylabel(r"$\Delta x$ (m)")
    axes[0].grid(True)

    axes[1].plot(t, delta_theta, color="tomato")
    axes[1].axhline(np.pi / 4, color="grey", ls="--", label=r"$\theta(0) = \pi/4$")
    axes[1].set_title(r"Angle d'inclinaison $\Delta\theta(t)$")
    axes[1].set_xlabel("temps $t$ (s)")
    axes[1].set_ylabel(r"$\Delta\theta$ (rad)")
    axes[1].grid(True)
    axes[1].legend()

    plt.tight_layout()
    plt.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We simulate the linearized lateral system with no control input:

    \[
    \phi(t)=0
    \quad \text{for all } t.
    \]

    The equations become

    \[
    \Delta\ddot{x} = -g\,\Delta\theta,
    \]

    \[
    \Delta\ddot{\theta} = 0,
    \]

    with initial conditions

    \[
    \Delta x(0)=0,
    \qquad
    \Delta\dot{x}(0)=0,
    \]

    \[
    \Delta\theta(0)=\frac{\pi}{4},
    \qquad
    \Delta\dot{\theta}(0)=0.
    \]

    ---

    ### Evolution of the tilt angle

    Since

    \[
    \Delta\ddot{\theta}=0,
    \]

    the angular velocity remains constant. Because

    \[
    \Delta\dot{\theta}(0)=0,
    \]

    we obtain

    \[
    \Delta\dot{\theta}(t)=0,
    \]

    thus

    \[
    \Delta\theta(t)=\frac{\pi}{4}.
    \]

    Therefore, the tilt angle stays constant for all time.
    On the graph, \(\Delta\theta(t)\) is a horizontal line equal to \(\pi/4\).

    ---

    ### Evolution of the lateral position

    The lateral dynamics are

    \[
    \Delta\ddot{x}=-g\,\Delta\theta.
    \]

    Since \(\Delta\theta=\pi/4\) is constant, the horizontal acceleration is constant:

    \[
    \Delta\ddot{x}
    =
    -\frac{g\pi}{4}.
    \]

    Integrating twice with zero initial position and velocity gives

    \[
    \Delta x(t)
    =
    -\frac{g\pi}{8}t^2.
    \]

    Thus, the lateral position follows a parabola and diverges quadratically with time.

    On the graph, \(\Delta x(t)\) continuously drifts sideways faster and faster.

    ---

    ### What do we see? How do we explain it?

    We observe that the tilt angle remains constant while the horizontal position diverges.

    This happens because there is no control input acting on the reactor angle \(\phi\). As a result, the initial tilt is never corrected.

    A booster tilted at \(45^\circ\) with no correction on \(\phi\) produces a constant horizontal thrust component. Since nothing corrects the tilt angle, the booster keeps accelerating sideways indefinitely, it would eventually crash.

    This shows that the open-loop system is unstable and that an active controller is required to stabilize the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The control law is

    \[
    \Delta\phi(t) = -Kz(t)
    \]

    with

    \[
    z =
    \begin{pmatrix}
    \Delta x \\
    \Delta \dot{x} \\
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{pmatrix}
    \]

    and

    \[
    K =
    \begin{pmatrix}
    0 & 0 & k_3 & k_4
    \end{pmatrix}.
    \]

    Therefore,

    \[
    \Delta\phi(t)
    =
    -k_3\Delta\theta(t)
    -
    k_4\Delta\dot{\theta}(t).
    \]

    The first two coefficients are zero because we deliberately ignore \(\Delta x\) and \(\Delta\dot{x}\).
    For now, we only want to stabilize the tilt angle.

    ---

    The rotational dynamics are

    \[
    \Delta\ddot{\theta}
    =
    -\frac{Mg\ell}{2J}\Delta\phi.
    \]

    Substituting the control law gives

    \[
    \Delta\ddot{\theta}
    =
    \frac{Mg\ell}{2J}
    \left(
    k_3\Delta\theta
    +
    k_4\Delta\dot{\theta}
    \right).
    \]

    To obtain a stable damped oscillator, the feedback must act in the opposite direction of the tilt.
    Thus, in practice, we choose negative gains in the matrix \(K\):

    \[
    K =
    \begin{pmatrix}
    0 & 0 & -k_3 & -k_4
    \end{pmatrix}.
    \]

    Then

    \[
    \Delta\phi(t)
    =
    k_3\Delta\theta(t)
    +
    k_4\Delta\dot{\theta}(t),
    \]

    and the closed-loop angular equation becomes

    \[
    \Delta\ddot{\theta}
    +
    \frac{Mg\ell}{2J}k_4\Delta\dot{\theta}
    +
    \frac{Mg\ell}{2J}k_3\Delta\theta
    =
    0.
    \]

    With

    \[
    M=1,\qquad g=1,\qquad \ell=2,\qquad J=\frac13,
    \]

    we have

    \[
    \frac{Mg\ell}{2J}=3.
    \]

    Hence,

    \[
    \Delta\ddot{\theta}
    +
    3k_4\Delta\dot{\theta}
    +
    3k_3\Delta\theta
    =
    0.
    \]

    This is a damped oscillator of the form

    \[
    \ddot{\theta}
    +
    2\zeta\omega_n\dot{\theta}
    +
    \omega_n^2\theta
    =
    0.
    \]

    Thus,

    \[
    \omega_n = \sqrt{3k_3},
    \]

    and

    \[
    \zeta =
    \frac{3k_4}{2\omega_n}.
    \]

    ---


    ## Design strategy for simulation

    We now choose the gains manually in order to satisfy the specifications:

    - convergence in about \(20\) seconds or less,
    - no excessive oscillations,
    - constraints
      \[
      |\Delta\theta(t)|<\frac{\pi}{2},
      \qquad
      |\Delta\phi(t)|<\frac{\pi}{2}.
      \]

    For a second-order system, the approximate settling time is

    \[
    T_{conv}
    \approx
    \frac{4}{\zeta\omega_n}.
    \]

    To obtain convergence in less than \(20\) seconds, we need

    \[
    \zeta\omega_n
    \geq
    \frac{4}{20}
    =
    0.2.
    \]

    To avoid overshoots, we choose a critically damped or over-damped response:

    \[
    \zeta \geq 1.
    \]

    We start with

    \[
    \omega_n=\sqrt{1.5}\approx1.22.
    \]

    Using

    \[
    \omega_n^2 = 3k_3,
    \]

    we obtain

    \[
    k_3
    =
    \frac{1.5}{3}
    =
    0.5.
    \]

    Then, using

    \[
    2\zeta\omega_n = 3k_4,
    \]

    with \(\zeta=1\), we get

    \[
    k_4
    =
    \frac{2\times1\times1.22}{3}
    \approx0.8.
    \]

    ---

    ## Iterative tuning

    ### First attempt

    \[
    k_3=1.0,
    \qquad
    k_4=1.0.
    \]

    This produces a relatively fast response, but the damping is insufficient and oscillations appear.
    The control input may also become too large.

    ---

    ### Second attempt

    \[
    k_3=0.5,
    \qquad
    k_4=1.0.
    \]

    The system becomes over-damped and oscillations disappear.
    However, convergence remains a bit slow (about \(25\) seconds).

    ---

    ### Final attempt

    \[
    k_3=0.5,
    \qquad
    k_4=2.0.
    \]

    This produces a strongly damped response:

    - no oscillations,
    - convergence in less than \(20\) seconds,
    - bounded control input,


    Therefore, the final controller is

    \[
    \boxed{
    K=
    \begin{pmatrix}
    0 & 0 & -0.5 & -2.0
    \end{pmatrix}
    }
    \]

    (the minus signs come from the convention
    \(\Delta\phi=-Kz\)).

    ---

    ## Closed-loop stability

    The closed-loop system is

    \[
    \dot z
    =
    A_{cl}z,
    \]

    with

    \[
    A_{cl}
    =
    A_{lat}-B_{lat}K.
    \]

    The closed-loop model is asymptotically stable if all eigenvalues of \(A_{cl}\) have strictly negative real parts:

    \[
    \operatorname{Re}(\lambda_i)<0
    \qquad
    \forall i.
    \]

    We verify this numerically in the simulation code below.
    The final closed-loop model is not asymptotically stable.
    """)
    return


@app.cell
def _(la, np, plt, sci):
    # Constants
    g_lat = 1.0
    M_lat = 1.0
    l_lat = 2.0
    J_lat = M_lat * l_lat**2 / 12

    # Reduced lateral matrices
    A_lat_new = np.array([
        [0, 1,  0, 0],
        [0, 0, -g_lat, 0],
        [0, 0,  0, 1],
        [0, 0,  0, 0],
    ])

    B_lat_new = np.array([
        [0],
        [-g_lat],
        [0],
        [-(M_lat * g_lat * l_lat) / (2 * J_lat)],
    ])

    # Initial condition
    z0_lat = np.array([0.0, 0.0, 45 / 180 * np.pi, 0.0])

    t_span_lat = [0.0, 25.0]
    t_lat = np.linspace(t_span_lat[0], t_span_lat[1], 1000)

    # Controller guesses
    K_list_lat = [
        np.array([[0.0, 0.0, -1.0, -1.0]]),
        np.array([[0.0, 0.0, -0.5, -1.0]]),
        np.array([[0.0, 0.0, -0.5, -2.0]]),
    ]

    labels_lat = [
        r"$k_3=1.0,\ k_4=1.0$",
        r"$k_3=0.5,\ k_4=1.0$",
        r"$k_3=0.5,\ k_4=2.0$ final",
    ]

    fig_lat, axes_lat = plt.subplots(1, 3, figsize=(16, 4))

    for K_lat, label_lat in zip(K_list_lat, labels_lat):

        A_cl_lat = A_lat_new - B_lat_new @ K_lat

        def closed_loop_lat(t_local, z_local):
            return A_cl_lat @ z_local

        sol_lat = sci.solve_ivp(
            closed_loop_lat,
            t_span_lat,
            z0_lat,
            dense_output=True
        )

        z_t_lat = sol_lat.sol(t_lat)

        delta_x_lat = z_t_lat[0]
        delta_theta_lat = z_t_lat[2]

        delta_phi_lat = (-K_lat @ z_t_lat).squeeze()

        axes_lat[0].plot(t_lat, delta_theta_lat, label=label_lat)
        axes_lat[1].plot(t_lat, delta_phi_lat, label=label_lat)
        axes_lat[2].plot(t_lat, delta_x_lat, label=label_lat)

    axes_lat[0].axhline(np.pi / 2, color="grey", ls="--")
    axes_lat[0].axhline(-np.pi / 2, color="grey", ls="--")
    axes_lat[0].set_title(r"Tilt angle $\Delta\theta(t)$")
    axes_lat[0].set_xlabel("time t")
    axes_lat[0].set_ylabel(r"$\Delta\theta$")
    axes_lat[0].grid(True)
    axes_lat[0].legend()

    axes_lat[1].axhline(np.pi / 2, color="grey", ls="--")
    axes_lat[1].axhline(-np.pi / 2, color="grey", ls="--")
    axes_lat[1].set_title(r"Control input $\Delta\phi(t)$")
    axes_lat[1].set_xlabel("time t")
    axes_lat[1].set_ylabel(r"$\Delta\phi$")
    axes_lat[1].grid(True)
    axes_lat[1].legend()

    axes_lat[2].set_title(r"Lateral position $\Delta x(t)$")
    axes_lat[2].set_xlabel("time t")
    axes_lat[2].set_ylabel(r"$\Delta x$")
    axes_lat[2].grid(True)
    axes_lat[2].legend()

    plt.tight_layout()
    plt.show()

    # Final controller
    K_final_lat = np.array([[0.0, 0.0, -0.5, -2.0]])
    A_cl_final_lat = A_lat_new - B_lat_new @ K_final_lat

    eigvals_lat = la.eigvals(A_cl_final_lat)
    real_parts_lat = np.real(eigvals_lat)
    print("Final K =", K_final_lat)
    print("Closed-loop eigenvalues =", eigvals_lat)
    print("Real parts =", np.real(eigvals_lat))
    if np.all(real_parts_lat < 0):
        print("Le système est asymptotiquement stable.")
    else:
        print("Le système n'est pas asymptotiquement stable.")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Design parameters

    The design parameters are the closed-loop poles:

    \[
    -0.5 \pm 0.5i,
    \qquad
    -0.3 \pm 0.3i.
    \]

    They are chosen to force the closed-loop system to have a stable and reasonably slow behavior.

    For a linear system

    \[
    \dot z = A_{lat}z + B_{lat}u,
    \]

    with feedback

    \[
    u = -K_{pp}z,
    \]

    the closed-loop system becomes

    \[
    \dot z = (A_{lat}-B_{lat}K_{pp})z.
    \]

    So the behavior of the system depends on the eigenvalues of

    \[
    A_{cl}=A_{lat}-B_{lat}K_{pp}.
    \]

    ---

    ### Why choose poles with negative real parts?

    A pole with negative real part makes the corresponding motion decay with time.

    So we choose all poles with

    \[
    \operatorname{Re}(\lambda)<0
    \]

    to obtain an asymptotically stable closed-loop system.

    ---

    ### Why choose complex conjugate poles?

    The system is real, so complex poles must appear in conjugate pairs.

    The imaginary part creates oscillations, while the real part makes these oscillations decay.

    That is why we choose

    \[
    -0.5 + 0.5i
    \quad\text{and}\quad
    -0.5 - 0.5i,
    \]

    and similarly

    \[
    -0.3 + 0.3i
    \quad\text{and}\quad
    -0.3 - 0.3i.
    \]

    ---

    ### How were the values chosen?

    The real parts \(-0.5\) and \(-0.3\) are not too close to zero, so the system converges in a reasonable time.

    They are also not too negative, which avoids a very aggressive controller and helps keep

    \[
    |\Delta\phi(t)| < \frac{\pi}{2}.
    \]

    The imaginary parts \(0.5\) and \(0.3\) give a moderate oscillatory response.

    So the poles are chosen as a compromise between:

    - fast convergence,
    - limited oscillations,
    - bounded control input,
    - and stability.

    ---
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt):
    def pole_placement_simulation():

        from scipy.signal import place_poles
        from scipy.integrate import solve_ivp

        # --- Choix des pôles ---
        poles_pp = np.array([
            -0.5 + 0.5j,
            -0.5 - 0.5j,
            -0.3 + 0.3j,
            -0.3 - 0.3j,
        ])

        # --- Calcul de K ---
        result = place_poles(A_lat, B_lat, poles_pp)
        K_pp = result.gain_matrix

        print("K_pp =", K_pp)

        A_cl_pp = A_lat - B_lat @ K_pp

        eig_pp = np.linalg.eigvals(A_cl_pp)

        print("Pôles obtenus :", sorted(eig_pp, key=lambda z: z.real))
        print("Stable :", all(ev.real < 0 for ev in eig_pp))

        # --- Simulation ---
        z0_local = [0.0, 0.0, 45/180 * np.pi, 0.0]

        t_span_local = [0.0, 40.0]

        t_local = np.linspace(*t_span_local, 2000)

        def cl_pp(t, z):
            u = -K_pp @ z
            return (A_lat @ z).reshape(4) + (B_lat @ u).reshape(4)

        sol_local = solve_ivp(
            cl_pp,
            t_span_local,
            z0_local,
            dense_output=True
        )

        z_t_local = sol_local.sol(t_local)

        delta_x_local = z_t_local[0]
        delta_theta_local = z_t_local[2]
        delta_phi_local = -(K_pp @ z_t_local)[0]

        print(
            f"max |Δθ| = {np.max(np.abs(delta_theta_local)):.3f} rad"
        )

        print(
            f"max |Δφ| = {np.max(np.abs(delta_phi_local)):.3f} rad"
        )

        # --- Graphes ---
        fig_local, axes_local = plt.subplots(1, 3, figsize=(15, 4))

        fig_local.suptitle(
            f"Pole Placement — K_pp = {np.round(K_pp, 3)}",
            fontsize=12
        )

        axes_local[0].plot(t_local, delta_x_local)
        axes_local[0].set_title(r"$\Delta x(t)$")
        axes_local[0].grid(True)

        axes_local[1].plot(t_local, delta_theta_local)
        axes_local[1].axhline(np.pi/2, color="grey", ls="--")
        axes_local[1].axhline(-np.pi/2, color="grey", ls="--")
        axes_local[1].set_title(r"$\Delta \theta(t)$")
        axes_local[1].grid(True)

        axes_local[2].plot(t_local, delta_phi_local)
        axes_local[2].axhline(np.pi/2, color="grey", ls="--")
        axes_local[2].axhline(-np.pi/2, color="grey", ls="--")
        axes_local[2].set_title(r"$\Delta \phi(t)$")
        axes_local[2].grid(True)

        plt.tight_layout()

        return plt.gcf()

    pole_placement_simulation()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Choice of the design parameters

    For the optimal controller, the design parameters are the matrices

    \[
    Q
    \quad \text{and} \quad
    R.
    \]

    The controller minimizes the quadratic cost function

    \[
    J
    =
    \int_0^{+\infty}
    \left(
    z(t)^TQz(t)
    +
    u(t)^TRu(t)
    \right)dt,
    \]

    where

    \[
    z =
    \begin{pmatrix}
    \Delta x \\
    \Delta\dot{x} \\
    \Delta\theta \\
    \Delta\dot{\theta}
    \end{pmatrix},
    \qquad
    u=\Delta\phi.
    \]

    The matrix \(Q\) penalizes the state errors, while \(R\) penalizes the control effort.

    ---

    ### Choice of \(Q\)

    We choose

    \[
    Q =
    \operatorname{diag}(5,\ 1,\ 20,\ 2).
    \]

    The largest weight is placed on

    \[
    \Delta\theta,
    \]

    because stabilizing the tilt angle is the most important objective.
    A tilted booster quickly becomes unstable, so we strongly penalize angular deviations.

    We also penalize

    \[
    \Delta x,
    \]

    because unlike the manually tuned controller, we now want the lateral position to converge toward zero.

    Smaller weights are used for the velocities

    \[
    \Delta\dot{x}
    \quad \text{and} \quad
    \Delta\dot{\theta},
    \]

    because they are less critical than the position and angle themselves.

    ---
    ### Why is the largest weight placed on \(\Delta\theta\)?

    We choose the largest weight:

    \[
    20
    \]

    for the tilt angle because the angle is the most critical variable.

    If the booster remains tilted:

    - it becomes unstable,
    - it generates horizontal thrust,
    - and it may crash.

    Therefore, we want

    \[
    \Delta\theta(t)\to0
    \]

    as quickly as possible.

    ### Choice of \(R\)

    We choose

    \[
    R = 50.
    \]

    A larger value of \(R\) penalizes large control inputs.

    This is important because we must satisfy the constraint

    \[
    |\Delta\phi(t)| < \frac{\pi}{2}.
    \]

    If \(R\) is too small, the controller becomes too aggressive and may generate unrealistically large reactor angles.

    If \(R\) is too large, the controller becomes too weak and convergence becomes too slow.

    Therefore, \(R=50\) is chosen as a compromise between:

    - fast stabilization,
    - smooth control,
    - and respecting the input constraints.

    ---

    ## Iterative tuning process

    The matrices \(Q\) and \(R\) are tuned iteratively by running simulations and observing:

    - the convergence speed of
      \[
      \Delta x(t)
      \quad \text{and} \quad
      \Delta\theta(t),
      \]

    - the amplitude of the control input
      \[
      \Delta\phi(t),
      \]

    - and the stability of the closed-loop system.

    Several values were tested:

    - increasing the weight on \(\Delta\theta\) accelerates angular stabilization,
    - increasing the weight on \(\Delta x\) reduces lateral drift,
    - increasing \(R\) reduces the control effort but slows down the response.

    The final choice gives:

    - asymptotic stability,
    - convergence in less than about \(20\) seconds,
    - bounded control input,
    - and satisfaction of the required constraints.

    ---

    ## Computation of the gain matrix

    Once \(Q\) and \(R\) are chosen, the gain matrix \(K_{oc}\) is computed automatically by solving the continuous-time Riccati equation:

    \[
    A^TP + PA - PBR^{-1}B^TP + Q = 0.
    \]

    The optimal gain is then

    \[
    K_{oc}
    =
    R^{-1}B^TP.
    \]

    The closed-loop dynamics become

    \[
    \dot z
    =
    (A_{lat}-B_{lat}K_{oc})z.
    \]

    Finally, we verify numerically that all eigenvalues of

    \[
    A_{lat}-B_{lat}K_{oc}
    \]

    have strictly negative real parts, which confirms that the closed-loop system is asymptotically stable.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt):
    def optimal_control_simulation():

    
        import scipy.linalg as sla
        from scipy.integrate import solve_ivp

        # --- Design parameters for optimal control ---
        Q_oc = np.diag([
            5.0,    # weight on Delta x
            1.0,    # weight on Delta x_dot
            20.0,   # weight on Delta theta
            2.0     # weight on Delta theta_dot
        ])

        R_oc = np.array([[50.0]])  # weight on Delta phi

        # --- Riccati equation ---
        P_oc = sla.solve_continuous_are(A_lat, B_lat, Q_oc, R_oc)

        # --- Gain matrix ---
        K_oc = np.linalg.inv(R_oc) @ B_lat.T @ P_oc

        print("K_oc =", K_oc)

        # --- Closed-loop matrix ---
        A_cl_oc = A_lat - B_lat @ K_oc

        eig_oc = np.linalg.eigvals(A_cl_oc)

        print("Pôles obtenus :", sorted(eig_oc, key=lambda z: z.real))
        print("Stable :", all(ev.real < 0 for ev in eig_oc))

        # --- Simulation ---
        z0_local = [0.0, 0.0, 45 / 180 * np.pi, 0.0]

        t_span_local = [0.0, 40.0]
        t_local = np.linspace(*t_span_local, 2000)

        def cl_oc(t, z):
            u = -K_oc @ z
            return (A_lat @ z).reshape(4) + (B_lat @ u).reshape(4)

        sol_local = solve_ivp(
            cl_oc,
            t_span_local,
            z0_local,
            dense_output=True
        )

        z_t_local = sol_local.sol(t_local)

        delta_x_local = z_t_local[0]
        delta_theta_local = z_t_local[2]
        delta_phi_local = -(K_oc @ z_t_local)[0]

        print(
            f"max |Δθ| = {np.max(np.abs(delta_theta_local)):.3f} rad"
        )

        print(
            f"max |Δφ| = {np.max(np.abs(delta_phi_local)):.3f} rad"
        )

        print(
            "Constraint |Δθ| < π/2:",
            np.max(np.abs(delta_theta_local)) < np.pi / 2
        )

        print(
            "Constraint |Δφ| < π/2:",
            np.max(np.abs(delta_phi_local)) < np.pi / 2
        )

        # --- Graphes ---
        fig_local, axes_local = plt.subplots(1, 3, figsize=(15, 4))

        fig_local.suptitle(
            f"Optimal Control — K_oc = {np.round(K_oc, 3)}",
            fontsize=12
        )

        axes_local[0].plot(t_local, delta_x_local)
        axes_local[0].axhline(0, color="grey", ls="--")
        axes_local[0].set_title(r"$\Delta x(t)$")
        axes_local[0].grid(True)

        axes_local[1].plot(t_local, delta_theta_local)
        axes_local[1].axhline(np.pi / 2, color="grey", ls="--")
        axes_local[1].axhline(-np.pi / 2, color="grey", ls="--")
        axes_local[1].set_title(r"$\Delta \theta(t)$")
        axes_local[1].grid(True)

        axes_local[2].plot(t_local, delta_phi_local)
        axes_local[2].axhline(np.pi / 2, color="grey", ls="--")
        axes_local[2].axhline(-np.pi / 2, color="grey", ls="--")
        axes_local[2].set_title(r"$\Delta \phi(t)$")
        axes_local[2].grid(True)

        plt.tight_layout()

        return plt.gcf()

    optimal_control_simulation()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We now test both controllers on the true nonlinear model.

    The controllers were designed using the linearized lateral model, but they must also work on the nonlinear booster dynamics.

    For both strategies, we use the nonlinear solver `redstart_solve` with

    \[
    f = Mg
    \]

    and

    \[
    \phi(t) = -Kz(t),
    \]

    where

    \[
    z(t)=
    \begin{pmatrix}
    x(t)\\
    \dot{x}(t)\\
    \theta(t)\\
    \dot{\theta}(t)
    \end{pmatrix}.
    \]

    We also saturate the control input to keep

    \[
    |\phi(t)| < \frac{\pi}{2}.
    \]

    The goal is to check that:

    \[
    x(t)\to0,
    \qquad
    \theta(t)\to0,
    \]

    and that the booster remains physically meaningful during the simulation.
    """)
    return


if __name__ == "__main__":
    app.run()
