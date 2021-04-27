# -*- coding: utf-8 -*-
"""
<parameters>
    <company>d.gavrilov</company>
    <title>association_orion</title>
    <version>1.0.8</version>
    <parameter>
        <name>Настройка вывода камер</name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>SERVER_ORION</id>
        <name>Сервер с Orion</name>
        <type>server</type>
    </parameter>
    <parameter>
        <id>MON</id>
        <name>Монитор для отображения</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>ALARM_TEMPLATE_AFTER</id>
        <name>Шаблон после тревоги</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>TIMEOUT</id>
        <name>Таймаут до сброса тревоги (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>STOP_SENSOR_TIME</id>
        <name>Задержка на повторную реакцию на событие от датчика (сек)</name>
        <type>integer</type>
        <min>1</min>
        <max>9999</max>
        <value>1</value>
    </parameter>
    <parameter>
        <id>EVENT_ORION</id>
        <type>string</type>
        <name>Cобытие</name>
        <value>Armed</value>
    </parameter>
    <parameter>
        <id>DEBUG</id>
        <name>Логирование</name>
        <type>boolean</type>
        <value>0</value>
    </parameter>
    <parameter>
        <name>Настройка ассоциаций </name>
        <type>caption</type>
    </parameter>
    <parameter>
        <id>ORION_1</id>
        <name>Датчик Орион-1</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_1</id>
        <name>Каналы  к Датчику Орион-1</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_2</id>
        <name>Датчик Орион-2</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_2</id>
        <name>Каналы  к Датчику Орион-2</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_3</id>
        <name>Датчик Орион-3</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_3</id>
        <name>Каналы к Датчику Орион-3</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_4</id>
        <name>Датчик Орион-4</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_4</id>
        <name>Каналы к Датчику Орион-4</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_5</id>
        <name>Датчик Орион-5</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_5</id>
        <name>Каналы к Датчику Орион-5</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_6</id>
        <name>Датчик Орион-6</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_6</id>
        <name>Каналы к Датчику Орион-6</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_7</id>
        <name>Датчик Орион -7</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_7</id>
        <name>Каналы к Датчику Орион-7</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_8</id>
        <name>Датчик Орион -8</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_8</id>
        <name>Каналы к Датчику Орион-8</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_9</id>
        <name>Датчик Орион -9</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_9</id>
        <name>Каналы к Датчику Орион-9</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_10</id>
        <name>Датчик Орион -10</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_10</id>
        <name>Каналы к Датчику Орион-10</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_11</id>
        <name>Датчик Орион -11</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_11</id>
        <name>Каналы к Датчику Орион-11</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_12</id>
        <name>Датчик Орион -12</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_12</id>
        <name>Каналы к Датчику Орион-12</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_13</id>
        <name>Датчик Орион -13</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_13</id>
        <name>Каналы к Датчику Орион-13</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_14</id>
        <name>Датчик Орион -14</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_14</id>
        <name>Каналы к Датчику Орион-14</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_15</id>
        <name>Датчик Орион -15</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_15</id>
        <name>Каналы к Датчику Орион-15</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_16</id>
        <name>Датчик Орион -16</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_16</id>
        <name>Каналы к Датчику Орион-16</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_17</id>
        <name>Датчик Орион -17</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_17</id>
        <name>Каналы к Датчику Орион-17</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_18</id>
        <name>Датчик Орион -18</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_18</id>
        <name>Каналы к Датчику Орион-18</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_19</id>
        <name>Датчик Орион -19</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_19</id>
        <name>Каналы к Датчику Орион-19</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_20</id>
        <name>Датчик Орион -20</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_20</id>
        <name>Каналы к Датчику Орион-20</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_21</id>
        <name>Датчик Орион -21</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_21</id>
        <name>Каналы к Датчику Орион-21</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_22</id>
        <name>Датчик Орион -22</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_22</id>
        <name>Каналы к Датчику Орион-22</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_23</id>
        <name>Датчик Орион -23</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_23</id>
        <name>Каналы к Датчику Орион-23</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_24</id>
        <name>Датчик Орион -24</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_24</id>
        <name>Каналы к Датчику Орион-24</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_25</id>
        <name>Датчик Орион -25</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_25</id>
        <name>Каналы к Датчику Орион-25</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_26</id>
        <name>Датчик Орион -26</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_26</id>
        <name>Каналы к Датчику Орион-26</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_27</id>
        <name>Датчик Орион -27</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_27</id>
        <name>Каналы к Датчику Орион-27</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_28</id>
        <name>Датчик Орион -28</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_28</id>
        <name>Каналы к Датчику Орион-28</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_29</id>
        <name>Датчик Орион -29</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_29</id>
        <name>Каналы к Датчику Орион-29</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_30</id>
        <name>Датчик Орион -31</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_30</id>
        <name>Каналы к Датчику Орион-30</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_31</id>
        <name>Датчик Орион -31</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_31</id>
        <name>Каналы к Датчику Орион-31</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_32</id>
        <name>Датчик Орион -32</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_32</id>
        <name>Каналы к Датчику Орион-32</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_33</id>
        <name>Датчик Орион -33</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_33</id>
        <name>Каналы к Датчику Орион-33</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_34</id>
        <name>Датчик Орион -34</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_34</id>
        <name>Каналы к Датчику Орион-34</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_35</id>
        <name>Датчик Орион -35</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_35</id>
        <name>Каналы к Датчику Орион-35</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_36</id>
        <name>Датчик Орион -36</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_36</id>
        <name>Каналы к Датчику Орион-36</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_37</id>
        <name>Датчик Орион -37</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_37</id>
        <name>Каналы к Датчику Орион-37</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_38</id>
        <name>Датчик Орион -38</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_38</id>
        <name>Каналы к Датчику Орион-38</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_39</id>
        <name>Датчик Орион -39</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_39</id>
        <name>Каналы к Датчику Орион-39</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_40</id>
        <name>Датчик Орион -40</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_40</id>
        <name>Каналы к Датчику Орион-40</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_41</id>
        <name>Датчик Орион -41</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_41</id>
        <name>Каналы к Датчику Орион-41</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_42</id>
        <name>Датчик Орион -42</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_42</id>
        <name>Каналы к Датчику Орион-42</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_43</id>
        <name>Датчик Орион -43</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_43</id>
        <name>Каналы к Датчику Орион-43</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_44</id>
        <name>Датчик Орион -44</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_44</id>
        <name>Каналы к Датчику Орион-44</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_45</id>
        <name>Датчик Орион -45</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_45</id>
        <name>Каналы к Датчику Орион-45</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_46</id>
        <name>Датчик Орион -46</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_46</id>
        <name>Каналы к Датчику Орион-46</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_47</id>
        <name>Датчик Орион -47</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_47</id>
        <name>Каналы к Датчику Орион-47</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_48</id>
        <name>Датчик Орион -48</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_48</id>
        <name>Каналы к Датчику Орион-48</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_49</id>
        <name>Датчик Орион -49</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_49</id>
        <name>Каналы к Датчику Орион-49</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_50</id>
        <name>Датчик Орион -50</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_50</id>
        <name>Каналы к Датчику Орион-50</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_51</id>
        <name>Датчик Орион -51</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_51</id>
        <name>Каналы к Датчику Орион-51</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_52</id>
        <name>Датчик Орион -52</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_52</id>
        <name>Каналы к Датчику Орион-52</name>
        <type>objects</type>
    </parameter>
>
    <parameter>
        <id>ORION_53</id>
        <name>Датчик Орион -53</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_53</id>
        <name>Каналы к Датчику Орион-53</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_54</id>
        <name>Датчик Орион -54</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_54</id>
        <name>Каналы к Датчику Орион-54</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_55</id>
        <name>Датчик Орион -55</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_55</id>
        <name>Каналы к Датчику Орион-55</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_56</id>
        <name>Датчик Орион -56</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_56</id>
        <name>Каналы к Датчику Орион-56</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_57</id>
        <name>Датчик Орион -57</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_57</id>
        <name>Каналы к Датчику Орион-57</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_58</id>
        <name>Датчик Орион -58</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_58</id>
        <name>Каналы к Датчику Орион-58</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_59</id>
        <name>Датчик Орион -59</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_59</id>
        <name>Каналы к Датчику Орион-59</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_60</id>
        <name>Датчик Орион -60</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_60</id>
        <name>Каналы к Датчику Орион-60</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_61</id>
        <name>Датчик Орион -61</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_61</id>
        <name>Каналы к Датчику Орион-61</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_62</id>
        <name>Датчик Орион -62</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_62</id>
        <name>Каналы к Датчику Орион-62</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_63</id>
        <name>Датчик Орион -63</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_63</id>
        <name>Каналы к Датчику Орион-63</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_64</id>
        <name>Датчик Орион -64</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_64</id>
        <name>Каналы к Датчику Орион-64</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_65</id>
        <name>Датчик Орион -65</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_65</id>
        <name>Каналы к Датчику Орион-65</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_66</id>
        <name>Датчик Орион -66</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_66</id>
        <name>Каналы к Датчику Орион-66</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_67</id>
        <name>Датчик Орион -67</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_67</id>
        <name>Каналы к Датчику Орион-67</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_68</id>
        <name>Датчик Орион -68</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_68</id>
        <name>Каналы к Датчику Орион-68</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_69</id>
        <name>Датчик Орион -69</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_69</id>
        <name>Каналы к Датчику Орион-69</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_70</id>
        <name>Датчик Орион -70</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_70</id>
        <name>Каналы к Датчику Орион-70</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_71</id>
        <name>Датчик Орион -71</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_71</id>
        <name>Каналы к Датчику Орион-71</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_72</id>
        <name>Датчик Орион -72</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_72</id>
        <name>Каналы к Датчику Орион-72</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_73</id>
        <name>Датчик Орион -73</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_73</id>
        <name>Каналы к Датчику Орион-73</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_74</id>
        <name>Датчик Орион -74</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_74</id>
        <name>Каналы к Датчику Орион-74</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_75</id>
        <name>Датчик Орион -75</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_75</id>
        <name>Каналы к Датчику Орион-75</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_76</id>
        <name>Датчик Орион -76</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_76</id>
        <name>Каналы к Датчику Орион-76</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_77</id>
        <name>Датчик Орион -77</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_77</id>
        <name>Каналы к Датчику Орион-77</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_78</id>
        <name>Датчик Орион -78</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_78</id>
        <name>Каналы к Датчику Орион-78</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>ORION_79</id>
        <name>Датчик Орион -79</name>
        <type>objects</type>
    </parameter>

    <parameter>
        <id>CHANNEL_79</id>
        <name>Каналы к Датчику Орион-79</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>ORION_80</id>
        <name>Датчик Орион -80</name>
        <type>objects</type>
    </parameter>
    <parameter>
        <id>CHANNEL_80</id>
        <name>Каналы к Датчику Орион-80</name>
        <type>objects</type>
    </parameter>
    <resources>
        <resource>helpers.py</resource>
        <resource>script_object.py</resource>
        <resource>base_object/base_object.py</resource>
        <resource>base_object/icons.py</resource>
        <resource>base_object/__init__.py</resource>
    </resources>
</parameters>
"""

GLOBALS = globals()
DEBUG = GLOBALS.get("DEBUG", False)
SERVER_ORION = GLOBALS.get("SERVER_ORION", "")
MON = GLOBALS.get("MON", 1)
ALARM_TEMPLATE_AFTER = GLOBALS.get("ALARM_TEMPLATE_AFTER", "")
TIMEOUT = GLOBALS.get("TIMEOUT", 1)
STOP_SENSOR_TIME = GLOBALS.get("STOP_SENSOR_TIME", 1)
EVENT_ORION = GLOBALS.get("EVENT_ORION", "Взять под охрану")

import helpers

helpers.set_script_name()
logger = helpers.init_logger("association_orion", debug=DEBUG)

import host
import json
from script_object import ScriptObject
from datetime import datetime, timedelta

orion_event = None
if EVENT_ORION:
    orion_event = set(ev_type.strip() for ev_type in EVENT_ORION.split(","))
else:
    raise ValueError("Необходимо указать события!")

obj = ScriptObject()


class AlarmMonitor:
    """
    Loop show channel and check old
    """

    def __init__(self, attention_monitor, alarm_template_after, time_to_del):
        self.attention_monitor = attention_monitor
        self.operate_gui = host.object("operatorgui_" + host.settings("").guid)
        self.chan_on_template = []
        for tmpl in host.settings("templates").ls():
            if tmpl.type == "Template" and tmpl.name == alarm_template_after:
                alarm_template_after_content = tmpl["content"]
                break
        else:
            raise RuntimeError("Шаблон не найден")

        self.alarm_template_after = alarm_template_after
        self.alarm_template_after_content = alarm_template_after_content
        self.time_to_del = time_to_del
        self.time_dict = {}

    def attention(self, guid_list):
        self.time_dict[datetime.now()] = guid_list
        for guid in guid_list:
            if guid in self.chan_on_template:
                logger.debug("has already")
                continue
            self.chan_on_template.append(guid)
        logger.debug(self.chan_on_template)
        self.show_chans()

    def show_chans(self):
        logger.debug("go to show %s" % self.chan_on_template)
        if len(self.chan_on_template) > 9:
            self.del_old()
            return
        try:
            self.operate_gui.show(
                "gui7(DEWARP_SETTINGS,,,-1,%s)"
                % ",".join(str(x) for x in self.chan_on_template),
                self.attention_monitor,
            )
        except Exception as e:
            logger.debug("ERROR to assign channels: %s" % e)
        host.timeout(1000 * self.time_to_del, self.del_old)

    def del_old(self):
        for time_, list_ in self.time_dict.copy().iteritems():
            if time_ + timedelta(seconds=self.time_to_del) < datetime.now():
                for channel in list_:
                    if channel in self.chan_on_template:
                        self.chan_on_template.remove(channel)
                del self.time_dict[time_]
        if not self.chan_on_template:
            logger.debug("stop alarm")
            self.operate_gui.show_template(
                self.alarm_template_after, self.attention_monitor
            )
            self.operate_gui.show(
                self.alarm_template_after_content, self.attention_monitor
            )


class OrionArmed:
    """collect orion association dict and catch event orion"""

    def __init__(
        self,
        monitor,
        alarm_template_after,
        time_to_del,
        stop_sensor_time,
        server_orion,
    ):
        self.orion_assotiation = {}
        self.temp_dict = {}
        self.stop_sensor_time = stop_sensor_time
        self.server_orion = server_orion
        self.alarm_obj = AlarmMonitor(monitor, alarm_template_after, time_to_del)
        self.__collect_orion()

    def __collect_orion(self):

        for x in xrange(1, 10000):
            sensor = GLOBALS.get("ORION_%s" % x)
            channels = GLOBALS.get("CHANNEL_%s" % x)
            if sensor is None:
                break

            if not sensor or not channels:
                continue

            sensor_guid = self.find_sensor(sensor)
            channel_guid_list = self.find_channel(channels)
            self.orion_assotiation[sensor_guid] = channel_guid_list
        logger.debug(self.orion_assotiation)
        assert self.orion_assotiation, "Необходимо выбрать датчик!"

    def find_sensor(self, name_orion):
        sensor_guid = ""
        for sett_orion in host.settings("/%s/orion" % self.server_orion).ls():
            if sett_orion.type == "OrionNode":
                for sett_sensor in sett_orion.ls():
                    if (
                        sett_sensor.type == "OrionNode"
                        and name_orion == sett_sensor.name
                    ):
                        sensor_guid = sett_sensor.guid
                        break
        return sensor_guid

    @staticmethod
    def check_access(sett):
        try:
            channel_name = sett.name
            return True
        except ValueError:
            pass

    def find_channel(self, str_channel):
        channels_list = str_channel.split(",")
        channels_guid_list = []
        for srv in host.settings("/").ls():
            if srv.type in ["LocalServer", "RemoteServer"]:
                for sett_chan in host.settings("/%s/channels" % srv.guid).ls():
                    if self.check_access(sett_chan):
                        if sett_chan.name in channels_list:
                            channels_guid_list.append("%s_%s" % (sett_chan.guid, srv.guid))
        return channels_guid_list

    def catch_event(self, ev):
        sensor = ev.origin
        if sensor in self.temp_dict:
            if self.temp_dict[sensor] >= datetime.now() - timedelta(
                seconds=self.stop_sensor_time
            ):
                return
        logger.debug(sensor)
        logger.debug(self.temp_dict)
        for sens in self.temp_dict.copy():
            if self.temp_dict[sens] <= datetime.now() - timedelta(
                seconds=self.stop_sensor_time
            ):
                del self.temp_dict[sens]
        alarm_list = self.orion_assotiation.get(sensor)
        logger.debug("%s сработал для каналов %s" % (sensor, alarm_list))
        if alarm_list:
            obj.fire_event_v2("Association Orion", data=json.dumps({"associated_channel": alarm_list, "ev_type": ev.type}))
            self.alarm_obj.attention(alarm_list)
            self.temp_dict[sensor] = datetime.now()
            host.stats()["run_count"] += 1


if not all([ALARM_TEMPLATE_AFTER, SERVER_ORION]):
    raise ValueError("Заполните параметры!")

oa = OrionArmed(MON, ALARM_TEMPLATE_AFTER, TIMEOUT, STOP_SENSOR_TIME, SERVER_ORION)

for event in orion_event:
    host.activate_on_events(event, "", oa.catch_event)
